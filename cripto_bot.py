import requests
import json

class Criptoconsulta:

    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"
        self.historico_file = 'historico.json'



    def consultar_preco(self, cripto):

        # Fazendo a requisição GET para a API
        resposta = requests.get(self.url.format(cripto))

        # Verificando se a requisição foi bem-sucedida (status code 200)
        if resposta.status_code == 200:
            dados = resposta.json()

            # Verificando se a criptomoeda existe na resposta
            if cripto in dados:
                # Verificando se a chave 'usd' existe na criptomoeda
                if 'usd' in dados[cripto]:
                    preco = dados[cripto]['usd']
                    variacao = dados[cripto].get('usd_24h_change', 'N/A')  # Se a variação não existir, coloca 'N/A'

                    print(f"\n{cripto.capitalize()}")
                    print(f"Preço: ${preco}")
                    print(f"Variação nas ultimas 24 horas: {variacao}%")
                else:
                    print(f"Não foi possível obter o preço em USD para {cripto}.")
            else:
                print(f"A criptomoeda {cripto} não foi encontrada.")

        else:
            print("Erro ao consultar preço. Tente novamente.")


    def salvar_no_historico(self, cripto):


            # Abrir o arquivo para ler os dados existentes
            with open('historico.json', "r") as arquivo:
                try:
                    historico = json.load(arquivo)

                except json.JSONDecodeError:
                    # Se o arquivo não existir, é criado um novo histórico vazio
                    historico = []


            # Adiciona a criptomoeda consultada ao histórico
            if cripto not in historico:
                historico.append(cripto)

             # Salva o histórico de volta no arquivo
            with open('historico.json', "w") as arquivo:
                json.dump(historico, arquivo, indent = 4)


    def exibir_historico(self):

            with open("historico.json", "r") as arquivo:
                historico = json.load(arquivo)

                if historico:
                    print("\nHistorico de consulta:")
                    for cripto in historico:
                        print(f"{cripto.capitalize()}")
                else: 
                    print("\nAinda não há historico de consultas.")


    # MENU
    def menu(self):
        while True:
            print("\n=== Menu de Criptomoedas ===\n")
            print("1 - Consultar preço de criptomoedas.")
            print("2 - Acessar historico de consultas.")
            print("3 - Sair.")

            opcao = input("\nDigite uma opção:" ).strip()

            if opcao == "1":
                cripto = input("Digite o nome da Criptomoeda (ex: bitcoin, ethereum): ").lower()
                self.consultar_preco(cripto)
                self.salvar_no_historico(cripto)

            elif opcao == "2":
                self.exibir_historico()

            elif opcao == "0":
                print("Saindo do programa...")
                break

            else:
                print("Opção invalida")


#Execução do programa
cripto_app = Criptoconsulta()
cripto_app.menu()

