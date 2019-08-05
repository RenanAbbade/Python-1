
def menu():
    opcao = int(input(
        "Escolha uma opcão: \n (1) Cadastrar um amigo (no final da lista) \n (2) Mostrar os nomes de todos os amigos\n (3) Cadastrar um amigo (no início da lista)\n (4) Remover um nome \n(5) Substituir um nome \n(6) Mostrar o número total de amigos cadastrados \n(7) Colocar os nomes dos amigos em ordem alfabética \n(8) Sair do programa \n"))
    while opcao<1 or opcao>8:
      opcao = int(input(
        "Escolha uma opcão correta: \n (1) Cadastrar um amigo (no final da lista) \n (2) Mostrar os nomes de todos os amigos\n (3) Cadastrar um amigo (no início da lista)\n (4) Remover um nome \n(5) Substituir um nome \n(6) Mostrar o número total de amigos cadastrados \n(7) Colocar os nomes dos amigos em ordem alfabética \n(8) Sair do programa \n"))
    if opcao == 1:
        cadastro(lista)
    elif opcao == 2:
      mostrarAmigos(lista)
    elif opcao == 3:
      cadastraramigoem1(lista)
    elif opcao == 4:
      removernome(lista)
    elif opcao == 5:
      substituirnome(lista)
    elif opcao == 6:
      mostrarnumerocadastrados(lista)
    elif opcao == 7:
      ordemalfabetica(lista)
    elif opcao == 8:
      print("Você escolheu sair ")
    else:
      print("Digite um número válido  ")

    return opcao


def cadastro(lista):

    amigo = input("Digite o novo nome a ser acrescentado na lista: \n")
    lista.append(amigo)
    menu()

def cadastraramigoem1(lista):
    amigocad = input("Digite o novo nome a ser acrescentado na lista, desta vez na primeira posição: \n")
    lista.insert(0,amigocad)
    print("Agora sua lista está assim: \n",lista)
    menu()
    
def removernome(lista):
  print(lista)
  deletado = int(input("Digite o número que representa a palavra a ser deletado, lembrando que eles estão numerados começando por 0 e da esquerda p/ direita: \n"))
  del lista[deletado]
  print("Agora sua lista está assim: \n",lista)
  menu()
  

def substituirnome(lista):
  print(lista)
  sub = int(input("Digite o número que representa a palavra a ser substituida, lembrando que eles estão numerados começando por 0 e da esquerda p/ direita: \n"))
  palavra = input("Agora digite a palavra que substituira a anterior: \n")
  lista[sub] = palavra
  print("Agora sua lista está assim: \n",lista)
  menu()

def mostrarnumerocadastrados(lista):
  print("Agora sua lista está assim: \n",lista)
  n = len(lista)
  print("Seu número de itens na lista é :", n)
  menu()

def ordemalfabetica(lista):
  print("Sua lista, anteriormente : \n",lista)
  lista.sort()
  print("Agora, em ordem alfabética! \n",lista)
  menu()
  



def mostrarAmigos(lista):
    print("Amigos da lista", lista)
    menu()






"------------"

lista = []
menu()





