from afip import Afip

CUIT = 20430075641

afip = Afip({ "CUIT": CUIT })

# Usuario para ingresar a AFIP.
# Para la mayoria es el mismo CUIT, pero al administrar
# una sociedad el CUIT con el que se ingresa es el del administrador
# de la sociedad.
username = ""

# Contraseña para ingresar a AFIP.
password = ""

# Alias para el certificado (Nombre para reconocerlo en AFIP)
# un alias puede tener muchos certificados, si estas renovando
# un certificado pordes utilizar le mismo alias
cert_alias = "afipsdk"

wsid = "wsfe"

# Creamos la autorizacion (¡Paciencia! Esto toma unos cuantos segundos)
res = afip.createWSAuth(username, password, cert_alias, wsid)

# Mostramos el resultado por pantalla
print(res)