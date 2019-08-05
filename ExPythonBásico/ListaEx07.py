'''
Exercicio 07 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017
'''

#ENTRADA
n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
n3 = float(input("Digite a terceira nota "))
n4 = float(input("Digite a quarta nota "))

#PROCESSAMENTO
media = (n1*7+n2*3+n3*6+n4*4)/20
if media >=7.5:
    print("Aprovado com nota de ", media)
else:
    print("Reprovado com nota de ", media)