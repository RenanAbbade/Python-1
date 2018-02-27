'''Exercicio 08 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
# ENTRADA
A = float(input("Digite o valor do primeiro lado "))
B = float(input("Digite o valor do segundo lado "))
C = float(input("Digite o valor do terceiro lado "))
# PROCESSAMENTO AND SAIDA
if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        print("Triângulo equilátero ")
    elif A == B and B != C or A == C and C != B or B == C and C != A:
        print("isósceles ")
    else:
        print("escaleno")
else:
    print("Um lado do triangulo não poderá ser maior que a soma dos outros dois lados! ")
