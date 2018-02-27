import math
'''

Renan Abbade
17/08/2017
Exercicio 11

'''
#ENTRADA
area = float(input("Qual o tamanho em metros da area a ser pintada? "))

#PROCESSAMENTO
lata = area/54
custo = lata*80

#SAIDA
print("A quantidade de latas, e o preço total será respectivamente ", "Número de lata", math.ceil(lata),"custo",custo)
