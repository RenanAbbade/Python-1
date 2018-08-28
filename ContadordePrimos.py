'''Vamos ampliar o problema de cálculo de números primos. Dados n números inteiros positivos, escreva um programa para calcular a soma dos que são primos. O seu programa deve usar necessariamente todas as funções criadas anteriormente.
A função somaPrimos recebe como entrada a quantidade de números qtd e retorna um inteiro representando a soma dos primos.'''


#Função identificar Primos
def contadorPrimos(n):
    ndiv = 0
    cont = 1
    while cont <= n:
        resto = n % cont
        if resto == 0:
            ndiv = ndiv + 1
        cont = cont + 1

    if ndiv == 1 or ndiv == 2:
        return True
    else:
        return False

#Função Somar Primos

def somar(qtd):
    cont2 = 0
    for i in range(qtd):
        y = int(input("Digite um número inteiro: "))
        if contadorPrimos(y) == True:
            cont2 = cont2+y
    return cont2


# função principal

qtd = int(input("Digite a quantidade de termos para somar os primos: "))

print('A quantidade de termos que você somou foi: {} a Soma dos primos é de: {}'.format(qtd,somar(qtd)))
