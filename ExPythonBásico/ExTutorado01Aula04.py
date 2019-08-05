import math

#ENTRADA


a = float(input("Escreva o primeiro número "))
b = float(input("Escreva o segundo número da equação "))
x = float(input("Escreva o número da variavel x "))

#PROCEDIMENTO

y = (math.pow(a,2)+math.sqrt(3*b))/(5*math.pow(x,3))

#SAIDA
print("O resultado da conta sera ", y)