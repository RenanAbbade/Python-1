'''
Ex 09 Aula 05 Extra
Digite um numero com 3 digitos no qual a saída mostre se o número da dezena é par ou impar
Author: Renan Abbade - 31782299 - 09/09/2017
'''
#ENTRADA
n1 = int(input("Digite um número de 3 digitos "))

#Processamento
dezenas = (n1%100)//10
if n1<100 or n1>999:
    print("Digite um número de 3 digitos!")
elif dezenas%2==0:
    print("Par")
else:
    print("Impar")