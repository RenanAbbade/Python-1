#ENTTRADA

valor = float(input("Digite o valor monetário "))


notas = valor/100
resto1 = valor%100

notas2 = resto1/50
resto2 = resto1%50

notas3 = resto2/20
resto3 = resto2%20

notas4 = resto3/10
resto4 = resto3%10

notas5 = resto4/5
resto5 = resto4%5

notas6 = resto5/2
resto6 = resto5%2

#moedas

notas7 = resto6/1
resto7 = resto6%1

notas8 = resto7/0.50
resto8 = resto7%0.50

notas9 = resto8/0.25
resto9 = resto8%0.25

notas10 = resto9/0.10
resto10 = resto9%0.10

notas11 = resto10/0.05
resto11 = resto10%0.05

notas12 = resto11/0.01
resto12 = resto11%0.01

print(format(notas,".0f"))
