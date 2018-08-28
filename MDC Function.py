'''12)	Escreva um algoritmo que calcule o MDC (máximo divisor comum) entre dois números naturais. O seu programa deve contar uma função que lê um número inteiro e positivo, bem como uma função, chamada MDC,  para calcular o MDC entre dois números inteiros e positivos e retornar o MDC entre eles.'''


def leNumero():
    num = int(input("Digite um número inteiro e positivos >0:   "))
    while num<=0:
        num = int(input("Digite um número inteiro e positivos >0: "))
    num2 = int(input("Digite o segundo número inteiro e positivos >0: "))
    while num2<=0:
        num2 = int(input("Digite o segundo número inteiro e positivos >0: "))
    
    return num, num2

def mDC(num,num2):
  #LogicaMMC
  if num>num2:
    maior = num
  else:
    maior = num2
  for i in range(1,maior):
    if num%i ==0 and num2%i == 0:
      mdc = i
  return mdc
    
     

    
#Função Principal

x, y = leNumero()
print("O mdc é:", mDC(x,y))