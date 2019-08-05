import random
''' Aula 06 Exercicio 02 Atividades de laboratório  - Author:Renan Abbade 31782299 10/09/2017
O Jogo do par ou ímpar é usado onde duas pessoas jogam geralmente para decidir um impasse,
cada um escolhe entre par ou ímpar e mostra o seu número, a soma entre eles resulta em um número par
ou ímpar e assim é decidido o vencedor. Aqui faremos com a máquina, ela escolherá um número randômico entre 0 e 10 e
você escolherá o seu.
Vamos ver quem é o vencedor!!!! '''
#ENTRADA
nome = input("Escreva seu nome ")
jogo = input("Digite par ou impar, se digitar diferente PC automaticamente vencerá ")
n1 = int(input(print("Escolha um número randômico entre 0 a 10, esse número e então de acordo com "
                     "sua primeira escolha par ou impar, será determinado o vencedor ")))
#PROCESSAMENTO
n2 = random.randint(0,10)
resultado = n1+n2
if n1>10 or n1<0:
    print("Número inválido, escolha um número de 0 a 10 ")
elif resultado%2==0 and jogo.upper()=='PAR':
    print(nome,"escolheu",n1,"e o PC",n2,"Resultado é",resultado,",Número par, jogador vencedor:",nome)
elif resultado %2!=0 and jogo.upper()=='IMPAR':
    print((nome,"escolheu",n1,"e o PC",n2,"Número impar, resultado é", resultado,"jogador vencedor é,",nome))
else:
    print(nome,"escolheu",n1,"PC escolheu",n2,",PC é o vencedor por escolher o jogo oposto de",nome)
