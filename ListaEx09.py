'''Exercicio 09 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
#ENTRADA
saldo_medio = float(input("Digite o valor do saldo médio do cliente "))


#PROCESSAMENTO
if saldo_medio>4000:
    print("O valor do crédito deste cliente será ", saldo_medio*30/100)
elif saldo_medio>=3000.01 and saldo_medio<=4000:
    print("O valor do crédito deste cliente será ", saldo_medio * 25 / 100)
elif saldo_medio>=2000.01 and saldo_medio<=3000:
    print("O valor do crédito deste cliente será ", saldo_medio * 20 / 100)
else:
    print("O valor do saldo médio será ", saldo_medio*10/100)

