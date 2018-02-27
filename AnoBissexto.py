'''
Faça um programa que receba um ano (quatro dígitos) e informe se é um ano bissexto ou não.
Pesquise quais as regras para o número ser bissexto.

Para ser bissexto, o ano deve ser:

Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
RENAN ABBADE 31/08/2017
'''
#ENTRADA
ano = int(input("Digite um ano com 4 digitos "))

#PROCESSAMENTO
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Este ano de",ano," é bissexto!")
else:
    print("O ano não é bissexto!!")
