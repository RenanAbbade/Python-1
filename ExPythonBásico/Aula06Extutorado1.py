#ENTRADA

A = int(input("Digite um numero "))
B = int(input("Digite um numero "))
C = int(input("Digite um numero "))

#PROCESSAMENTO

if A<B and A<C:
    print("O menor número é o primeiro ", A)
else:
    if B < A and B < C:
        print("O menor número é o segundo ", B)
    else:
        if C <A and C < B:
            print("O menor número é o terceiro ", C)



