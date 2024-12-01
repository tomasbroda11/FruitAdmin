from arca_auth import generar_ticket_acceso, obtener_token_y_sign

# Generar el XML firmado
xml_firmado = generar_ticket_acceso()

# Enviar el XML firmado y obtener el Token y Sign
resultado = obtener_token_y_sign(xml_firmado)
print("Token:", resultado["token"])
print("Sign:", resultado["sign"])
