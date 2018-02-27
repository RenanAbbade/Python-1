'''
Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente. A tabela
de preços do hospital é a seguinte:
 Quartos:
o Particular – R$ 360,00
o Semi-particular – R$ 210,00
o Coletivo – R$ 185,00
 WIFI: R$ 3,00
 TV a cabo: R$ 4,00
Escreva um programa que leia: o número de dias gastos no hospital; o tipo de quarto; se usou ou
não o WIFI (Sim, Não); se usou ou não a TV a cabo (Sim, Não). Então emita um relatório, como por
exemplo o seguinte:
Hospital Comunitário
Número de dias no hospital : 5
Tipo de quarto : Particular
Diárias :............... R$ 1800,00
WIFI :..... ....... R$ 3,00
TV a cabo :........... R$ 4,00
Total :................... R$ 1807,00

'''
#ENTRADA
dias = int(input("Digite o número de dias gastos no hospital "))
quarto = input("Digite sua opção : 1 -o Particular – R$ 360,00 2 - o Semi-particular – R$ 210,00 o 3 - Coletivo – R$ 185,00")
wifi = int(input("O cliente usou o wifi, responda (3)sim ou não(0)"))
tv = int(input("O cliente usou tv a cabo, (4)sim ou não(0)"))

#processamento

if quarto=='1':
    print("Diarias ->",360*dias,"wifi......3,00","tv a cabo....4,00","Total",(360*dias)+wifi+tv)
elif quarto=='2':
    print("Diarias ->",210*dias,"wifi 3,00","tv a cabo 4,00","Total",(210*dias)+tv+wifi)
elif quarto=='3':
    print("Diarias ->",185*dias,"wifi 3,00","tv a cabo 4,00","Total",(185*dias)+tv+wifi)
else
