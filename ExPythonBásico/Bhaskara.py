import math

#ENTRADA



a = float(input("Escreva o número de a "))
b = float(input("Escreva o número da variavel b"))
c = float(input("Escreva o número da variavel c "))

#procedimento

x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)


print("As raízes da equação são ", x1, "e", x2)