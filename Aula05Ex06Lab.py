'''Elabore um programa que leia do teclado o sexo de uma pessoa.
Se o sexo digitado for “M” ou “m” ou “F” ou “f”, escrever na tela “Sexo válido!”.
 Caso contrário, exibir “Sexo inválido!”. '''
#ENTRADA
sexo = input("Digite o seu sexo(M para masculino e F para feminino ")

#PROCESSAMENTO
if sexo.upper() == 'M' or sexo.upper()=='F':
    print("Sexo válido ")
else:
    print("Sexo inválido ")