import math
'''EX 02
EXERCICIO COM DISCUSSÃO EM DUPLAS 
Escreva um programa que leia dois números distintos e apresente o quadrado do maior número
Author Renan Abbade 31782299
'''
#ENTRADA
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))

#PROCESSAMENTO

if n1>n2:
  T = math.pow(n1,2)
  print("O quadraro do maior número será ", T )
elif n2>n1:
    R = math.pow(n2,2)
    print("O quadrado do maior número será ", R)

