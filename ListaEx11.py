'''Exercicio 11 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
# ENTRADA
consumo = int(input("Digite o consumo de água em metros cúbicos em sua residência "))

# PROCESSAMENTO

if consumo <= 10:
    print("O valor da conta de água será", "7,00 R$")
elif consumo >= 11 and consumo <= 30:

    print("O valor da conta de água será ", (consumo - 10) + 7)
elif consumo >= 31 and consumo <= 100:
    consumo2=((consumo - 30) * 2)
    print("O valor da conta de água será ", ((consumo - 30) * 2) + 7)
elif consumo >= 101:
    consumo1 = (30 - 10)
    consumo2 = ((100 - 30) * 2)
    consumo3 = ((consumo-100)*5)
    total = consumo1+consumo2+consumo3+7
    print("O valor da conta de água será ", total)


