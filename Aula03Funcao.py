''' -> Crie um programa que:
- Tenha uma função que apresente um menu de opções
- uma função que calcule a área do quadrado
- uma função que calcule a área do triangulo
- uma função que calcule a distancia entre os pontos A e B '''

'''Funções'''
def menuOpcoes():
    print("-------------MENU------------------ \n Digite 1 para calcular a area do quadrado \n Digite 2 para calcular a área do triangulo \n Digite 3 para calcular a distancia dos pontos A e B \n   ")

def areaQuadrado():
    lado = float(input("Digite o tamanho do lado do quadrado em Metros:  "))
    area_quadrado = lado**2
    return area_quadrado

def areaTriangulo():
    base = float(input("Digite o tamanho da base do triangulo em Metros:   "))
    altura = float(input("Digite o tamanho da altura do triangulo em Metros:    "))
    area_triangulo = (base * altura) / 2
    return area_triangulo

def distancia():
    A = float(input("Digite a localização do ponto A em Metros:   "))
    B = float(input("Digite a localização do ponto B em Metros:     "))
    dist = A-B
    return dist

'''----Programa Principal----'''
menuOpcoes()
opcao = int(input("Digite a opção desejada:  "))
while opcao<1 or opcao>3:
    opcao = int(input("Digite a opção desejada(valida entre um e três: \n\n "))
if opcao == 1:
    print('Resultado é:', areaQuadrado(),"Metros")
elif opcao == 2:
    print('Resultado é:', areaTriangulo(),"Metros")
elif opcao == 3:
    print('Resultado é:', distancia(),"Metros de distância")





