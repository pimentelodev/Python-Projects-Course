"""
-GRUPO BESOURO VERMELHO-
Naytson Pimentel da Silva
Edson Pedro da Rocha Silva
Eddie Yago Gabriel dos Santos Sátiro
Franco Alves Silva
Guilherme Natã Meirelles Jung
"""

condicao = 0

listaNome = []
listaMani = []

print("\nBem-vindo à Ouvidoria BESOURO VERMELHO.\n")

while condicao != 6:
    print("|============================================|")
    print("|        OUVIDORIA - MENU DE AÇÕES           |")
    print("|============================================|")
    print("| Opção | Descrição                          |")
    print("|   1   | Listar manifestações               |")
    print("|   2   | Criar uma nova manifestação        |")
    print("|   3   | Exibir quantidade de manifestações |")
    print("|   4   | Pesquisar manifestação por código  |")
    print("|   5   | Excluir manifestação por código    |")
    print("|   6   | Sair do sistema                    |")
    print("|============================================|")

    condicao = int(input("\nDigite a ação que deseja realizar: "))

    if condicao > 0 and condicao <= 5:
        if condicao == 1:
            print("1) Listar manifestações")
            if len(listaMani) == 0:
                print("\nNão há manifestações registradas ainda.\n")
            else:
                for item in range(len(listaMani)):
                    print(item + 1, "-", listaNome[item])
            print()

        elif condicao == 2:
            print("2) Criar uma nova manifestação")
            nomeMani = input("Digite seu nome completo: ")
            novaMani = input("Digite sua manifestação: ")
            listaNome.append(nomeMani)
            listaMani.append(novaMani)
            print("\nSua manifestação foi registrada com sucesso!\n")

        elif condicao == 3:
            print("3) Quantidade de manifestações")
            print("A quantidade de manifestações atualmente é:", len(listaNome))
            print()

        elif condicao == 4:
            print("4) Pesquisar manifestação por código")
            print()
            if len(listaNome) == 0:
                print("Não há manifestações registradas.")

            elif len(listaNome) != 0:
                pesquisa = int(input("Digite o código que deseja pesquisar:"))
                print()

                if pesquisa > 0 and pesquisa <= len(listaNome):
                    print("Manifestação registrada por", listaNome[pesquisa-1], ":")
                    print("(", listaMani[pesquisa-1], ")")
                    print()
                else:
                    print()
                    print("Este código não existe. Por favor, insira um código válido.")
                    print()

        elif condicao == 5:
            excluir2 = 10
            if len(listaNome) == 0:
                print("\nNão há manifestações para serem excluídas.\n")
            else:
                while excluir2 != 3:
                    print("5) Excluir uma manifestação por código")
                    excluir = int(input("Digite o número da manifestação que deseja excluir: "))
                    print()

                    if excluir >= 1 and excluir <= len(listaNome):
                        print("A manifestação a ser excluída é de:", listaNome[excluir - 1], "\n(", listaMani[excluir - 1], ")")
                        print()
                        print("Para excluir esta manifestação, digite 1.")
                        print("Para escolher outra manifestação, digite 2.")
                        print("Para voltar ao menu principal, digite 3.")
                        excluir2 = int(input("Escolha uma opção: "))
                        print()

                        if excluir2 == 1:
                            print("A manifestação de", listaNome[excluir - 1], "foi excluída com sucesso!")
                            listaMani.pop(excluir - 1)
                            listaNome.pop(excluir - 1)
                            excluir2 = 3
                            print()
                        elif excluir2 > 3 and excluir2 <= 0:
                            print("Opção inválida. Por favor, escolha outra opção.\n")
                    else:
                        print("Não há manifestação com este código.\nSelecione uma opção entre 1 e", len(listaMani))
                        print()

    elif condicao <= 0 or condicao > 6:
        print()
        print("Opção inválida. Por favor, digite novamente.\n")

print()
print("-----------------------------------------------------")
print("Agradecemos por utilizar a Ouvidoria BESOURO VERMELHO")
print("-----------------------------------------------------")