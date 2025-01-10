import sys
import os
from dotenv import load_dotenv

# Adicionar o diretório pai ao sys.path para importar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from modules.consultas import consultar_preco, consultar_historico_de_preco
from modules.historico import salvar_no_historico, exibir_historico
from modules.exportacao import exportar_para_csv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Credenciais do Twilio
TWILIO_PHONE = os.getenv('TWILIO_PHONE')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Função que envia mensagem de boas vindas
def send_welcome_message():
    resp = MessagingResponse()
    resp.message("Olá! Eu sou o seu assistente de criptomoedas. Aqui estão os comandos que você pode usar:\n"
                 "- 'preço de [criptomoeda]' - Para consultar o preço atual de uma criptomoeda (exemplo: 'preço de bitcoin').\n"
                 "- 'histórico' - Para visualizar o histórico das criptomoedas que você consultou.\n"
                 "- 'salvar [criptomoeda]' - Para salvar uma criptomoeda no seu histórico (exemplo: 'salvar bitcoin').\n"
                 "- 'ajuda' - Para ver essas instruções novamente.\n\n"
                 "Envie uma mensagem para começar!")
    return str(resp)

# Rota para verificar o status do servidor
@app.route("/", methods=['GET'])
def index():
    return "Server is running"

# Rota que vai receber as requisições POST
@app.route("/bot", methods=['POST', 'OPTIONS'])
def bot():
    if request.method == 'OPTIONS':
        return '', 200  # Handle preflight request

    incoming_msg = request.values.get('Body', '').lower()  # Mensagem recebida do usuario
    sender = request.values.get('From', '')  # Número do usuário

    resp = MessagingResponse()
    msg = resp.message()

    # Se for a primeira mensagem ou "start", enviar as intruções
    if incoming_msg == "start" or incoming_msg == "":
        return send_welcome_message()
    
    # Verifica o que o usuario enviou a mensagem e responde o usuario
    elif 'preço de' in incoming_msg:
        cripto = incoming_msg.split('de')[1].strip()
        preco_info = consultar_preco(cripto)
        if 'erro' in preco_info:
            msg.body(preco_info['erro'])
        else:
            msg.body(f"O preço atual de {cripto} é ${preco_info['preco']} USD, com uma variação de {preco_info['variacao']}% nas últimas 24 horas.")
            salvar_no_historico(cripto)
    
    elif 'histórico' in incoming_msg:
        historico = exibir_historico()
        if historico:
            msg.body("Histórico de consultas:\n" + "\n".join(historico))
        else:
            msg.body("Seu histórico está vazio.")
    
    elif 'salvar' in incoming_msg:
        cripto = incoming_msg.split('salvar')[1].strip()
        salvar_no_historico(cripto)
        msg.body(f"{cripto} foi salvo no seu histórico.")
    
    elif 'exportar' in incoming_msg:
        cripto = incoming_msg.split('exportar')[1].strip()
        exportar_para_csv(cripto)
        msg.body(f"Os dados de {cripto} foram exportados para CSV.")
    
    elif 'ajuda' in incoming_msg:
        return send_welcome_message()
    
    else:
        msg.body("Desculpe, não entendi a sua mensagem. Envie 'ajuda' para ver os comandos disponíveis.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)