import math
#ENTRADA

n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
n3 = int(input("Digite o terceiro número "))

#PROCEDIMENTO

soma = math.pow(n1,2)+math.pow(n2,2)+math.pow(n3,2)
soma2 = n1+n2+n3

#SAIDA
print("A soma do quadrado desses 3 números será", soma)
print("O quadrado da soma dos três números ", math.pow(soma2,2))