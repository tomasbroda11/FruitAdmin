import requests

url = "https://wsaahomo.afip.gov.ar/ws/services/LoginCms?wsdl"
file_path = r"C:\Users\tomas\OneDrive\Escritorio\certificados-testing-tomas\cert-chain-afip.pem"

response = requests.get(url, verify=file_path)

print("Status code:", response.status_code)
print("Response content:", response.text)
