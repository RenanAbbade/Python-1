'''
Aula 05 Exercicio 08 Extra
Elabore um programa que leia dois números reais e mostre o resultado da diferença do maior
valor pelo menor.
Author: Renan Abbade 31782299
'''
n1 = float(input("Digite um número "))
n2 = float(input("Digite um número "))

if n1>n2:
  print("Resultado da diferença do maior pelo menor",n1-n2)
else:
  print("Resultado da diferença do maior pelo menor",n2-n1)
