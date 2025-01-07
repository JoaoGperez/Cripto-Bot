from modules.consultas import consultar_preco, consultar_historico_de_preco
from modules.historico import salvar_no_historico, exibir_historico
from modules.exportacao import exportar_para_csv

def volta_ao_menu():
    continuar = None
    while continuar is None:
        try:
            continuar = int(input())
            if continuar == 0:
                return False
            elif continuar == 1:
                return True
        except ValueError:
            print("Opção inválida. Digite 1 ou 0.")
            continuar = None


    
 #   while (continuar == None):
 #       try:
 #           continuar = int(input())
 #           if (continuar == 0):
 #               continuar = False
 #           elif (continuar == 1):
 #               continuar = True
 #       except ValueError: 
 #           continue
 #   if (continuar == False):
 #       break



def exibir_menu():
    while True:
        print("\n=== Menu de Criptomoedas ===\n")
        print("1 - Consultar preço de criptomoedas.")
        print("2 - Acessar histórico de consultas.")
        print("3 - Acessar historico de preços de criptomoedas.")
        print("4 - Exportar dados para CSV")
        print("0 - Sair.")

        opcao = input("\nDigite uma opção: ").strip()
   

        if opcao == "1":
            while True:
                cripto = input("Digite o nome da Criptomoeda (ex: bitcoin, ethereum): ").lower()
                print(consultar_preco(cripto))
                salvar_no_historico(cripto)

                print("\n1 - Consultar outra criotomoeda.")
                print("0 - Voltar ao menu principal.")
                if not volta_ao_menu():
                    break

        elif opcao == "2":
            historico = exibir_historico()
            print("\nHistórico de consultas:")
            for cripto in historico:
                print(cripto)

        elif opcao == "3":
            while True:
                cripto = input("Digite o nome da Criptomoeda (ex: bitcoin, ethereum): ").lower()
                intervalo = input("Escolha o intervalo de tempo (24h, 7d, 30d): ")
                print(consultar_historico_de_preco(cripto, intervalo))

                print("\n1 - Consultar histórico de preço de outra criptomoeda.")
                print("0 - Voltar ao menu principal.")
                if not volta_ao_menu():
                    break

        elif opcao == "4":
            cripto = input("Digite o nome da criptomoeda para exportar os dados para CSV: ")
            exportar_para_csv(cripto)


        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida")
