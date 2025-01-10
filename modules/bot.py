import sys
import os
from dotenv import load_dotenv
from flask import Flask
from twilio.rest import Client

# Adicionar o diretório pai ao sys.path para importar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.routes import app  # Importação absoluta

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Credenciais do Twilio
TWILIO_PHONE = os.getenv('TWILIO_PHONE')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# Verificação das variáveis de ambiente
if not all([TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN]):
    raise ValueError("Por favor, defina as variáveis de ambiente TWILIO_PHONE, TWILIO_ACCOUNT_SID e TWILIO_AUTH_TOKEN no arquivo .env")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if __name__ == "__main__":
    app.run(debug=True)