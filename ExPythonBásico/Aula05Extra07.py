import math
'''
Ex 07 Extra
Escreva um programa que leia um número e apresente a raiz quadrada caso seja positivo ou
nulo, e o quadrado do número caso seja negativo.
math.sqrt(x) retorna a raiz quadrada de x
Author:Renan Abbade
'''
n1 = float(input("Digite um número "))

if n1>0 or n1==0:
  print("Raiz de número positivo ou nulo",math.sqrt(n1))
else:
   print("Número negativo ao quadrado ", math.pow(n1,2))
