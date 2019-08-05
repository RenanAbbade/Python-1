'''
Escreva um programa que faz a conversão de temperatura de Celsius para Farenheit e de
Farenheit para Celsius. Sugestão: utilize um caracter para definir em que unidade está a
temperatura dada pelo usuário.
C=5/9.( F-32)
F = C*9/5+32
'''
# ENTRADA
t1 = input("Digite Celsius C ou Farenheit F para  a conversão ")
t2 = input("Digite Celsius C ou Farenheit F para a conversão ")
temp = int(input("Digite o valor da temperatura "))
# processamento
if t1 == 'C' or t1 == 'c' and t2 == 'F' or t2 == 'f':
    # celsius p/ fahernheit
    Fa = temp * (9/5) + 32
    print("A conversão de celsius para farenheit será ",Fa)

if t1 == 'F' or t1 == 'f' and t2 == 'C' or t2 == 'c':
    Ce = (5/9)*( temp-32)
    print("A conversão de farenheit para celsius será ", Ce)

else:
    print("Digite C para Celsius ou F para farenheit!!!!!")