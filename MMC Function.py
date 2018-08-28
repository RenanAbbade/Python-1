def leNumero():
    num = int(input("Digite um número inteiro e positivos >0:   "))
    while num<=0:
        num = int(input("Digite um número inteiro e positivos >0: "))
    num2 = int(input("Digite o segundo número inteiro e positivos >0: "))
    while num2<=0:
        num2 = int(input("Digite o segundo número inteiro e positivos >0: "))
    
    return num, num2

def mmc(num,num2):
   #LogicaMMC
    if num > num2:
      maior = num
    else:
      maior = num2
    while True:
      if maior % num == 0 and maior % num2 == 0:
        return maior
      else:
        maior += 1

     

    
#Função Principal
x, y = leNumero()
print("O mmc é:", mmc(x,y))