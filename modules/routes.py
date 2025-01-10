from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from .helpers import send_welcome_message
from .consultas import consultar_preco
from .historico import salvar_no_historico, exibir_historico
from .exportacao import exportar_para_csv
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Server is running"

@app.route("/bot", methods=['POST', 'OPTIONS'])
def bot():
    if request.method == 'OPTIONS':
        return '', 200  # Handle preflight request

    incoming_msg = request.values.get('Body', '').lower()  # Mensagem recebida do usuario
    sender = request.values.get('From', '')  # Número do usuário

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "start" or incoming_msg == "":
        return send_welcome_message()
    
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