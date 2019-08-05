import math
#ENTRADA
custo = float(input("Digite o custo do espetáculo "))
convite = float(input("Digite o preço do convite "))

#PROCEDIMENTO

E = custo/convite
QTD = E*1.23

#SAIDA

print("Quantidade de convites que deve ser vendida ", math.ceil(E))
print("Quantidade para lucro de 23% ", math.ceil(QTD))



