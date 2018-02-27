import math

#ENTRADA


a = float(input("Escreva o primeiro número "))
b = float(input("Escreva o segundo número da equação "))
y = float(input("Escreva o número da variavel y "))

x = y+math.sqrt((2*b)/(a+b))

print("O resultado da função sera ", x)