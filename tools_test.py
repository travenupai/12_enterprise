import os
import requests
from crewai_tools import tool

HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")

@tool
def hunter_discover_search(location, industry, size, domain):
    # Discover search query
    url = f"https://api.hunter.io/v2/domain-search"
    params = {
        "domain": domain,
        "location": location,
        "industry": industry,
        "size": size,
        "api_key": HUNTER_API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        companies = response.json()
        return companies
    else:
        return f"Error: {response.status_code} - {response.text}"

# tipo de chamada:
# Exemplo de chamada
location = "Brazil"
industry = "Medical Practices"
size = "11-50"  # Tamanho da empresa (ou múltiplos, como "1-10,11-50")
domain = "exampledomain.com"

# Executando a função
companies = hunter_discover_search(location, industry, size, domain)
print(companies)





@tool
def hunter_email_finder(domain, first_name=None, last_name=None):
    # Email finder query
    url = f"https://api.hunter.io/v2/email-finder"
    params = {
        "domain": domain,
        "first_name": first_name,
        "last_name": last_name,
        "api_key": HUNTER_API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        emails = response.json()
        return emails
    else:
        return f"Error: {response.status_code} - {response.text}"

# tipo de chamada:
# Exemplo de chamada
domain = "exampledomain.com"
first_name = "John"
last_name = "Doe"

# Executando a função
emails = hunter_email_finder(domain, first_name=first_name, last_name=last_name)
print(emails)








@tool
def hunter_email_verifier(email):
    # Endpoint para verificar a validade do email
    url = "https://api.hunter.io/v2/email-verifier"
    params = {
        "email": email,
        "api_key": HUNTER_API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        verification = response.json()
        return verification
    else:
        return f"Error: {response.status_code} - {response.text}"
    
    
# tipo de chamada:
result = hunter_email_verifier("contato@empresa.com")
print(result)