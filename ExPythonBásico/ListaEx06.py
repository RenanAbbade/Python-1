'''

Exercicio 06 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017
8 Mbps = 1 MB/s
'''
#1 Mbps = 0.125 MB/s
#ENTRADA

arquivo = float(input("Qual o tamanho do arquivo para dowload? em MB "))
internet = float(input("Qual a velocidade de um link de internet?(em Mbps "))

#PROCESSAMENTO
velocidade = internet*0.125
tempo = arquivo/velocidade
minutos = tempo/60


#SAIDA
print("O tempo aproximado do dowload será de ", minutos, "minutos ou",tempo,"segundos")