'''Exercicio 01 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''

#ENTRADA
n1 = int(input("Digite um número qualquer "))
#processamento
centenas = n1//100
centenas1 = centenas%10
dezenas = (n1%100)//10
unidades = ((n1%100)%10)
#saida
print("Algarismo de centena", centenas1,"dezenas",dezenas,"unidades",unidades)