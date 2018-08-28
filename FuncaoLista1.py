
def menu():
    opcao = int(input(
        "Escolha uma opcão: \n (1)Cadastrar um amigo \n (2)Mostrar os nomes de todos os amigos cadastrados \n (8)Sair do programa"))
    if opcao == 1:
        cadastro(lista)
    elif opcao == 2:
      mostrarAmigos(lista)
    elif opcao == 8:
      print("Você escolheu sair ")
    else:
      print("Digite um número válido  ")

    return opcao


def cadastro(lista):

    amigo = input("Digite o novo nome a ser acrescentado na lista ")
    lista.append(amigo)
    menu()




def mostrarAmigos(lista):
    print("Amigos da lista", lista)
    menu()






"------------"

lista = []
menu()





