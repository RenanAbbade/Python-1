import math
#ENTRADA
# Volume de uma lata de óleo -> v = pi*r²

altura = float(input("Digite a altura do objeto "))
raio = float(input("Digite o raio do objeto "))

v = math.pi*math.pow(raio,2)*altura

print("O volume do objeto será ",v)
