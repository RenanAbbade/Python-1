import random
''' Aula 06 Ex 01 - atividade de laboratório 10/09 - author: Renan Abbade
 Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos, aposte em um número que seja o resultado da soma deles
e ganhe o seu dinheiro. Crie duas variáveis para representar os dados e uma para sua aposta,
 crie uma para armazenar o resultado e faça a verificação. '''
#ENTRADA
aposta = int(input("aposte em um número que seja o resultado da soma de dois dados e ganhe o seu dinheiro "))

#PROCESSAMENTO
dados1 = random.randint(1,6)
dados2 = random.randint(1,6)
resultado = dados1+dados2

#Saida
if aposta == resultado:
    print("Parabéns, você ganhou 1 milhão de dollares com sua aposta em",resultado)
else:
    print("Que azar!O número correto é",resultado)