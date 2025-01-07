import requests
from datetime import datetime, timedelta, timezone

import requests

def consultar_preco(cripto):
    url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd".format(cripto)
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if cripto in dados:
            preco = dados[cripto].get('usd', 'N/A')
            variacao = dados[cripto].get('usd_24h_change', 'N/A')
            return {'preco': preco, 'variacao': variacao}
        else:
            return {'erro': f"A criptomoeda {cripto} não foi encontrada."}
    else:
        return {'erro': "Erro ao consultar preço. Tente novamente."}

def consultar_historico_de_preco(cripto, intervalo):
     # Define a URL para consulta histórica
    url = f"https://api.coingecko.com/api/v3/coins/{cripto}/market_chart/range"

    # Calculando o timestamp do intervalo
    agora = datetime.now()
    if intervalo == "24h":
        inicio = agora - timedelta(days= 1)
    elif intervalo == "7d":
        inicio = agora - timedelta(days= 7)
    elif intervalo == "30d":
        inicio = agora - timedelta(days= 30)
    else:
        return "Intervalo invalido"


    # Convertendo para formato timestamp
    inicio_timestemp = int(inicio.timestamp())
    fim_timestemp = int (agora.timestamp())


    # Fazendo a requisição
    params = {"vs_currency": "usd", "from": inicio_timestemp, "to": fim_timestemp}
    resposta = requests.get(url, params = params)

    # Verifica se a requisição foi bem-sucedida.
    if resposta.status_code == 200:
        dados = resposta.json()

        # Obtem os preços historicos das respostas da API
        if 'prices' in dados:
            resultados = dados['prices']
            historico = "\nHistorico de preços: \n"

            for item in resultados:
                data = datetime.fromtimestamp(item[0] /1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                preco = item[1]
                historico += f'{data} - ${preco:.2f}\n'
                return historico

