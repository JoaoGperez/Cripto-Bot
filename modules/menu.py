from modules.consultas import consultar_preco, consultar_historico_de_preco
from modules.historico import salvar_no_historico, exibir_historico

def exibir_menu():
    while True:
        print("\n=== Menu de Criptomoedas ===\n")
        print("1 - Consultar preço de criptomoedas.")
        print("2 - Acessar histórico de consultas.")
        print("3 - Acessar historico de preços de criptomoedas.")
        print("0 - Sair.")

        opcao = input("\nDigite uma opção: ").strip()

        if opcao == "1":
            cripto = input("Digite o nome da Criptomoeda (ex: bitcoin, ethereum): ").lower()
            print(consultar_preco(cripto))
            salvar_no_historico(cripto)

        elif opcao == "2":
            historico = exibir_historico()
            print("\nHistórico de consultas:")
            for cripto in historico:
                print(cripto)

        elif opcao == "3":
            cripto = input("Digite o nome da Criptomoeda (ex: bitcoin, ethereum): ").lower()
            intervalo = input("Escolha o intervalo de tempo (24h, 7d, 30d): ")
            print(consultar_historico_de_preco(cripto, intervalo))

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida")
