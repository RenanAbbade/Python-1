'''
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da
compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Escreva um programa que
receba o valor do produto e exiba o valor da venda.

'''
#ENTRADA
valor = int(input("Digite o valor do produto "))


#PROCESSAMENTO
if valor<20:
    valor_venda = valor*1.45
    print("O valor de venda será ", valor_venda)
else:
    valor_venda2 = valor*1.30
    print("O valor de venda será", valor_venda2)
