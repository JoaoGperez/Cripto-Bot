import csv
from datetime import datetime
from modules.consultas import consultar_preco, consultar_historico_de_preco

def exportar_para_csv(cripto, arquivo_csv = 'dados_criptomoedas.csv'):
    
    #Consultar o preço atual
    preco_atual_info = consultar_preco(cripto)
    preco_atual = None

    if isinstance(preco_atual_info, dict):
        preco_atual = preco_atual_info.get('preco', 'N/A')
    else:
        raise ValueError(f"Consultar_preço não retornou um dicionario.")

    # Consultar o histórico de preços
    historico_24h = consultar_historico_de_preco(cripto, '24h')
    historico_7d = consultar_historico_de_preco(cripto, '7d')
    historico_30d = consultar_historico_de_preco(cripto, '30d')

    # Estrutura para os dados da tabela
    dados = {
        'criptomoeda': cripto,
        'preco_atual': preco_atual,
        'historico_24h': historico_24h,
        'historico_7d': historico_7d,
        'historico_30d': historico_30d,
        'Ultima Atualização': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Verificação de cabeçalho no csv
    try:
        with open('arquivo_csv', 'r') as arquivo:
            existe_cabecalho = csv.Sniffer().has_header(arquivo.read(1024))
    except FileNotFoundError:
        existe_cabecalho = False

    # Escrita no arquivo csv
    with open(arquivo_csv, mode = 'a', newline = '') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados.keys())

        # Adiciona cabeçalho se o arquivo for novo
        if not existe_cabecalho:
            escritor.writeheader()

        # Adiciona os dados de criptomoeda
        escritor.writerow(dados)
    
    print(f"Dados da criptomoeda {cripto} exportados para {arquivo_csv} com sucesso.")