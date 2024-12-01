import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

# Configuración inicial
WSAA_URL = "https://wsaahomo.afip.gov.ar/ws/services/LoginCms"  # URL del WSAA
SERVICE = "wsfe"  # Servicio para el que se solicita autenticación

def generar_tra(service):
    """
    Genera el Ticket de Requerimiento de Acceso (TRA).
    """
    tra = ET.Element('loginTicketRequest', {'version': '1.0'})
    header = ET.SubElement(tra, 'header')
    ET.SubElement(header, 'uniqueId').text = str(int(datetime.now(tz=timezone.utc).timestamp()))
    ET.SubElement(header, 'generationTime').text = (datetime.now(tz=timezone.utc) - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")
    ET.SubElement(header, 'expirationTime').text = (datetime.now(tz=timezone.utc) + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")
    ET.SubElement(header, 'service').text = service
    return ET.tostring(tra, encoding="utf-8")

def guardar_tra(tra, filename="TRA.xml"):
    """
    Guarda el TRA generado en un archivo.
    """
    with open(filename, "wb") as f:
        f.write(tra)
    print(f"TRA guardado en {filename}")

def obtener_token_y_sign(wsaa_url):
    """
    Lee el CMS firmado generado con OpenSSL y lo envía al WSAA.
    """
    # Leer el CMS firmado en Base64
    with open("TRA.base64", "r") as f:
        signed_tra = f.read().strip()

    # Validar que no tenga saltos de línea o caracteres extraños
    signed_tra = signed_tra.replace("\n", "").replace("\r", "")

    # Crear XML para WSAA
    envelope = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsaa="http://wsaa.view.sua.dvadac.desein.afip.gov">
    <soapenv:Header/>
    <soapenv:Body>
        <wsaa:loginCms>
            <wsaa:in0>{signed_tra}</wsaa:in0>
        </wsaa:loginCms>
    </soapenv:Body>
    </soapenv:Envelope>"""

    # Mostrar el XML generado para validación
    print("XML generado:")
    print(envelope)

    # Enviar la solicitud al WSAA
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": ""  # Encabezado requerido
    }
    response = requests.post(wsaa_url, data=envelope, headers=headers)

    # Analizar respuesta
    if response.status_code == 200:
        xml_response = ET.fromstring(response.content)
        token = xml_response.find(".//token").text
        sign = xml_response.find(".//sign").text
        return token, sign
    else:
        raise Exception(f"Error en la solicitud a WSAA: {response.text}")

# Flujo Principal
try:
    # Generar el TRA
    tra = generar_tra(SERVICE)
    guardar_tra(tra)

    print("Por favor, firma el archivo 'TRA.xml' con OpenSSL y genera el CMS en 'TRA.base64':")
    print("Comando para firmar con OpenSSL:")
    print("  openssl smime -sign -signer certificado-test1.txt -inkey keytest -in TRA.xml -out TRA.cms -outform DER -nodetach")
    print("Comando para convertir a Base64:")
    print("  openssl base64 -in TRA.cms -out TRA.base64")
    input("Presiona Enter cuando hayas firmado y generado el archivo 'TRA.base64'...")

    # Enviar el CMS al WSAA
    token, sign = obtener_token_y_sign(WSAA_URL)
    print(f"Token: {token}")
    print(f"Sign: {sign}")
except Exception as e:
    print(f"Error: {e}")
