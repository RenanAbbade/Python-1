#ENTRADA
produto = int(input("Digite o valor monetário "))



notas = produto//100
resto1 = produto%100

notas2 = resto1//50
resto2 = resto1%50

notas3 = resto2//20
resto3 = resto2%20

notas4 = resto3//10
resto4 = resto3%10

notas5 = resto4//5
resto5 = resto4%5

notas6 = resto5//2
resto6 = resto5%2

#moedas

notas7 = resto6//1
resto7 = resto6%1



print((format(notas,".0f")), "notas de R$ 100,00")
print((format(notas2,".0f")), "notas de R$ 50,00")
print((format(notas3,".0f")), "notas de R$ 20,00")
print((format(notas4,".0f")), "notas de R$ 10,00")
print((format(notas5,".0f")), "notas de R$ 5,00")
print((format(notas6,".0f")), "notas de R$ 2,00")
print((format(notas7,".0f")), "notas de R$ 1,00")
