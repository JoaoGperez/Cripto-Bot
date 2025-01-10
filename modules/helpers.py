from twilio.twiml.messaging_response import MessagingResponse


def send_welcome_message():
    """
    Envia uma mensagem de boas-vindas com instruções de uso.
    """
    resp = MessagingResponse()
    resp.message("Olá! Eu sou o seu assistente de criptomoedas. Aqui estão os comandos que você pode usar:\n"
                 "- 'preço de [criptomoeda]' - Para consultar o preço atual de uma criptomoeda (exemplo: 'preço de bitcoin').\n"
                 "- 'histórico' - Para visualizar o histórico das criptomoedas que você consultou.\n"
                 "- 'salvar [criptomoeda]' - Para salvar uma criptomoeda no seu histórico (exemplo: 'salvar bitcoin').\n"
                 "- 'ajuda' - Para ver essas instruções novamente.\n\n"
                 "Envie uma mensagem para começar!")
    return str(resp)