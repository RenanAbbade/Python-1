'''Author: Renan Henrique da Silva Abbade - 31782299  Aula 10 Ex.8'''
#ENTRADA
cont = 0
cont_e = 0
cont_m = 0
cont_f = 0
media_m = 0
vezes = int(input("Digite a quantidade de vezes: "))
for i in range(vezes):
    nome = input("Digite o nome do empregado: ")
    sexo = input("Digite o sexo do empregado: ")
    while sexo != "F" and sexo != "M":
        sexo = input("Digite o sexo do empregado: ")
    if sexo.upper()=="F":
        cont_f = cont_f+1
    salario = float(input("Digite o salário do empregado: "))
    while salario<850:
        salario = float(input("Digite o salário do empregado(acima de 850): "))
    if salario>=3000:
        salario = salario + salario*(4.5/100)
    if salario<3000 and salario>2000:
        salario = salario + salario * (6.5/ 100)
        cont_e =  cont_e+1
    if salario<2000:
        salario = salario + salario * (8.5 / 100)
    if sexo.upper() == "M":
        media_m = media_m+salario
        cont_m = cont_m + 1
    cont = cont + 1

print("Quantidade de empregados que receberam ajuste de 6.5%:",cont_e,"\n","Salario médio dos homens é",media_m/cont_m,"\n"," o percentual de empregados do sexo feminino ",cont_f*(100/cont),"%")







