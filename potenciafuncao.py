import math

def pot(): #Potenciação em Função
    x = int(input("Digite a base da potência:   "))
    p = int(input("Digite o expoente:    "))
    potencia = math.pow(x,p)
    return potencia

#PRINCIPAL

print(pot())