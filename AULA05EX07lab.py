'''
Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 2,5%
para carros fabricados antes de 2010 e uma taxa de 3,5% para os fabricados de 2010 em diante,
taxa esta incidindo sobre o valor de tabela do carro. Escreva um programa lê o ano e o preço
do carro e a seguir calcula e imprime a taxa a ser paga.
RENAN ABBADE 31/08/2017
'''
#ENTRADA
ano_carro = int(input("Digite o ano de seu carro "))
preco_carro = float(input("Digite o preço de seu carro "))

#PROCEDIMENTO
if ano_carro<2010:
    taxa = (2.5*preco_carro)/100
    print("O valor total da taxa a ser paga será", (format(taxa, ".2f")))
else:
    taxa = (3.5*preco_carro)/100
    print("O valor total da taxa a ser paga será",(format(taxa,".2f")))


