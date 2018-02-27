'''Um pescador comprou um computador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
do Estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente.
Escreva um programa que leia o peso de peixes, e verifique se há excesso. Se houver,
determine o peso excedente e o valor da multa. Caso contrário, mostrar “Dentro do
regulamento”.'''
#ENTRADA
peso_peixes = int(input("Digite o peso dos peixes "))


#ENTRADA
if peso_peixes>50:
    ex = peso_peixes-50
    print("Multa de quatro reais por peso excedente, o peso excedente(maior que 50) é",ex," valor da multa ficara ", 50+(ex*4))
else:
    print("Dentro do regulamento ")


