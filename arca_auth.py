import base64
import datetime
from zeep import Client
from zeep.transports import Transport
from requests import Session
from OpenSSL import crypto
from FruitAdmin import settings

# Configurar el cliente SOAP
session = Session()
session.verify =False
transport = Transport(session=session)
client = Client(settings.ARCA_WS_URL, transport=transport)


def generar_ticket_acceso():
    # Generar el XML base
    xml_template = """
    <loginTicketRequest version="1.0">
      <header>
        <uniqueId>{unique_id}</uniqueId>
        <generationTime>{generation_time}</generationTime>
        <expirationTime>{expiration_time}</expirationTime>
      </header>
      <service>wsfe</service>
    </loginTicketRequest>
    """
    now = datetime.datetime.now()
    xml_base = xml_template.format(
        unique_id=int(now.timestamp()),
        generation_time=(now - datetime.timedelta(minutes=5)).isoformat(),
        expiration_time=(now + datetime.timedelta(minutes=5)).isoformat(),
    )

    # Firmar el XML base
    with open(settings.ARCA_PRIVATE_KEY_PATH, "r") as key_file:
        private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, key_file.read())

    signature = crypto.sign(private_key, xml_base.encode("utf-8"), "sha256")
    signature_base64 = base64.b64encode(signature).decode("utf-8")

    # Leer el certificado y convertirlo a Base64
    with open(settings.ARCA_CERTIFICATE_PATH, "r") as cert_file:
        certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file.read())
        certificate_base64 = base64.b64encode(
            crypto.dump_certificate(crypto.FILETYPE_PEM, certificate)
        ).decode("utf-8")

    # Construir el XML firmado completo
    signed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <loginTicketRequest>
        <header>
            <uniqueId>{int(now.timestamp())}</uniqueId>
            <generationTime>{(now - datetime.timedelta(minutes=5)).isoformat()}</generationTime>
            <expirationTime>{(now + datetime.timedelta(minutes=5)).isoformat()}</expirationTime>
        </header>
        <service>wsfe</service>
        <signature>{signature_base64}</signature>
        <cert>{certificate_base64}</cert>
    </loginTicketRequest>
    """
    return signed_xml


def obtener_token_y_sign(xml_firmado):
    # Enviar el XML firmado al Web Service de Autenticación
    response = client.service.loginCms(xml_firmado)

    # Extraer el Token y el Sign de la respuesta
    from xml.etree import ElementTree as ET
    response_xml = ET.fromstring(response)
    token = response_xml.find(".//token").text
    sign = response_xml.find(".//sign").text

    return {"token": token, "sign": sign}
