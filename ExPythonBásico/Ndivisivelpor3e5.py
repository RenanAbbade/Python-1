'''
 Faça um programa que apresente se o número que o usuário digitou é divisível por 3 e por 5
ao mesmo tempo
31/08/2017
RENAN ABBADE
'''
#ENTRADA
n1 = float(input("Digite um número para vermos se é divisivel por 3 e 5  "))
#PROCESSAMENTO
if n1%3==0 and n1%5==0:
    print("Numero divisivel por 3 e por 5")

else:
    print("Não divisivel por 3 e 5")

