'''
Escreva um programa em Python que peça para o usuário digite um texto (mensagem: “Digite
um texto: ”) e depois para digitar um número (mensagem: “Digite um número”). Depois, deve
mostrar duas mensagens:1) “A primeira entrada é um dado do tipo <tipo>”; 2) “A segunda
entrada é do tipo <tipo>”, em que <tipo> deve ser trocado pelo tipo dos dados de entrada do
usuário.

Renan Abbade
17/08/2017
Exercicio 08

'''
#ENTRADA
texto = input("Digite um texto ")
numero = int(input("Digite um número qualquer "))

#SAIDA
print("A primeira entrada é tipo", type(texto), "A segunda entrada é tipo ", type(numero))



