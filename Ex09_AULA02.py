'''

Renan Abbade
17/08/2017
Exercicio 09

'''
#ENTRADA
qtd_km = int(input("Quantos km rodados? "))
qtd_dias = int(input("Quantos dias? "))

#processamento
custo = (qtd_km*0.15)+(qtd_dias*60)

#SAIDA
print("O custo total será ", custo)
