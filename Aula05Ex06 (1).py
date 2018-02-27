#31 de agosto de 2017 - Renan Henrique da Silva Abbade
#ENTRADA

n_maca=int(input("Digite o número de maçãs compradas "))

#PROCESSAMENTO

if n_maca<12:
    custo1 = n_maca*1.30
    print("O custo total de maçãs será de ",custo1)
if n_maca>=12:
    custo2 = n_maca*1
    print("O custo total será de ", custo2)
else:
    print("Digite um valor válido ")