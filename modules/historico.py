import json

def salvar_no_historico(cripto, historico_file='historico.json'):
    try:
        # Abrir o arquivo para ler os dados existentes
        with open(historico_file, "r") as arquivo:
            historico = json.load(arquivo)
    except json.JSONDecodeError:
        # Se o arquivo não existir, é criado um novo histórico vazio
        historico = []

    # Adiciona a criptomoeda consultada ao histórico
    if cripto not in historico:
        historico.append(cripto)

    # Salva o histórico de volta no arquivo
    with open(historico_file, "w") as arquivo:
        json.dump(historico, arquivo, indent=4)


def exibir_historico(historico_file='historico.json'):
    try:
        with open(historico_file, "r") as arquivo:
            historico = json.load(arquivo)
            
        return historico if historico else ["Ainda não há histórico de consultas."]
    except json.JSONDecodeError:
        return ["Ainda não há histórico de consultas."]
