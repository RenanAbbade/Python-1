'''

Renan Abbade
17/08/2017
Exercicio 10

'''
#ENTRADA
salario = float(input("Qual o salario do funcionario?"))
percentual = float(input("Qual o percentual de aumento?"))

#PROCESSAMENTO

aumento = salario*percentual/100
salario_novo = aumento+salario

#SAIDA

print("O salario novo será ", salario_novo)