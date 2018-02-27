'''Exercicio 04 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
#ENTRADA
custo = float(input("Digite o custo do espetáculo teatral "))
preco = float(input("Digite o preço do convite para este espetáculo "))
quantidade = int(input("Digite a quantidade de ingressos vendidos "))

#PROCESSAMENTO
#RENDA BRUTA = TOTAL ARRECADADO EXCLUINDO CUSTO
renda_bruta = preco*quantidade
print("Renda bruta é ", renda_bruta)

#RENDA LIQUIDA = TOTAL ARRECADADO MENOS CUSTO
renda_liquida = (preco*quantidade)-custo
print("Renda liquida é", renda_liquida)

#Lucro porcento
#renda bruta - 100%
#renda_liquida - x
x = renda_liquida*100/renda_bruta
print("Lucro em % é", (round(x,1)))