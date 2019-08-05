'''
 Elabore um programa que leia notas de três avaliações de um aluno. A primeira avaliação tem
peso 2, a segunda tem peso 3 e, a terceira, peso 5. Calcule a média do aluno. Se a média do
aluno for maior ou igual a 6, o aluno está aprovado; caso contrário, o aluno está reprovado.
Mostre o resultado da decisão.

'''

#ENTRADA
n1 = int(input("Digite a primeira nota "))
n2= int(input("Digite a segunda nota "))
n3 = int(input("Digite a terceira nota "))

#PROCESSAMENTO
nota1 = n1*2
nota2 = n2*3
nota3 = n3*5
media = nota1+nota2+nota3/3

if media>=6:
    print("Aluno aprovado ")
else:
    print("Aluno reprovado ")