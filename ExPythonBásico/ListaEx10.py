'''Exercicio 10 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
#Entrada
produto = float(input("Digite o preço a ser pago pelo produto "))
pagamento = input("Digite sua condição de pagamento: 1- Á vista em dinheiro ou cheque, recebe 10% de desconto / 2-  À vista no cartão de crédito, recebe 5% de desconto / 3-  Em 2 vezes, preço normal de etiqueta sem juros / 4- Em 3 vezes, preço normal de etiqueta mais juros de 10%")

#PROCESSAMENTO
if pagamento =='1':
    print("A vista com 10% de desconto ", format(produto*0.90,".2f"),"R$")
elif pagamento =='2':
    print("A vista no crédito com 5% de desconto ", format(produto*0.95,".2f"),"R$")
elif pagamento =='3':
    print("Em duas vezes, preço normal de etiqueta sem juros ",format(produto,".2f"),"R$")
elif pagamento =='4':
    print("Em três vezes, preço normal de etiquera com juros de 10% ", format(produto*1.10,".2f"),"R$")
else:
    print("Digite um número de 1 a 4 de acordo com as opções de pagamento. ")