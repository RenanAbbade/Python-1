'''Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e
 a escolha da condição de pagamento.Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida
 e efetuar o cálculo adequado.
Código Condições de pagamento 1- À vista em dinheiro ou cheque, recebe 10% de desconto
2- À vista no cartão de crédito, recebe 5% de desconto
 3 -Em 2 vezes, preço normal de etiqueta sem juros
4 -Em 3 vezes, preço normal de etiqueta mais juros de 10%
 Aula07 Ex02 Author Renan Abbade 11/09/2017'''
#ENTRADA
produto=float(input("Digite o preço da etiqueta do produto "))
pagamento=input("Escolha a opção de pagamento 1- À vista em dinheiro ou cheque, recebe 10% de desconto/- À vista no cartão de crédito, recebe 5% de desconto/3 -Em 2 vezes, preço normal de etiqueta sem juros/4 -Em 3 vezes, preço normal de etiqueta mais juros de 10% ")

#PROCESSAMENTO
if pagamento=='1':
    print("A vista em dinheiro ou cheque, recebe 10% de desconto, o preço será",produto*0.90)
elif pagamento=='2':
    print(" A vista no cartão de crédito, recebe 5% de desconto, o preço será", produto*0.95)
elif pagamento=='3':
    print("Em 2 vezes, preço normal de etiqueta sem juros:",produto," parcela no valor de",produto/2)
elif pagamento=='4':
    print("Em 3 vezes, preço normal de etiqueta mais juros de 10%:",format(produto*1.10,".2f")," o preço por parcela será ",format((produto*1.10)/3,".2f"))
else:
    print("Escolha uma opção de pagamento valida")
