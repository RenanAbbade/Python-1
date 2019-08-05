'''
Faça um programa que coloque dois nomes em ordem alfabética
RENAN ABBADE
31/08/2017
'''
#ENTRADA
nome1 = input("Digite o primeiro nome ")
nome2 = input("Digite o segundo nome ")

#PROCESSAMENTO
if nome1[0]<nome2[0]:
    print("Ordem alfabética ", nome1,nome2)
else:
    print("Ordem alfabética",nome2,nome1)
