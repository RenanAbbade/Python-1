import math
'''
Exercicio 02 lista de exercicios
Leia as coordenadas (x,y) de dois pontos no plano cartesiano, calcule e mostre a distância
entre os dois pontos.
Author:Renan Abbade 31782299 - 06/09/2017'

'''
#ENTRADA
x1 = float(input("Digite a coordenada do ponto x1 "))
x2 = float(input("Digite a coordenada do ponto x2 "))
y1 = float(input("Digite a coordenada do ponto y1" ))
y2 = float(input("Digite a coordenada do ponto y2 "))

#PROCESSAMENTO

d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2- y1,2))

print(" A diferença entre os dois pontos no plano cartesiano será de:",d)