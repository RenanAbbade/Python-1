'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?" b. "Esteve no local do crime?" c. "Mora perto da vítima?" d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
 Aula07 Ex02 Author Renan Abbade 11/09/2017'''
#ENTRADA
print("Responda com sim ou não")
a = input("Telefonou para a vitima? ")
b = input("Esteve no local do crime? ")
c = input("Mora perto da vitima? ")
d = input("Devia para a vitima? ")
e = input("Já trabalhou com a vítima? ")

#PROCESSAMENTO
if a.upper() and b.upper() and c.upper()=='NÃO' and d.upper() and e.upper()=='SIM' or a.upper() and c.upper and d.upper()=='NÃO' and b.upper() and e.upper()=='SIM' or a.upper() and d.upper() and e.upper() =='NÃO' and b.upper() and c.upper()=='SIM' or b.upper() and c.upper and d.upper() == 'NÃO' and a.upper() and e.upper()=='SIM' or b.upper() and d.upper and e.upper()=='NÃO' and a.upper() and c.upper()=='SIM' or c.upper() and d.upper() and e.upper()=='NÃO' and a.upper() and b.upper()=='SIM':
    print("Suspeita")
elif a.upper()and b.upper()=='NÃO' and c.upper() and d.upper() and e.upper()=='SIM' or a.upper() and c.upper()=='NÃO' and b.upper() and d.upper() and e.upper()=='SIM' or a.upper() and d.upper()=='NÃO' and c.upper() and b.upper() and e.upper()=='SIM' or a.upper()and e.upper()=='NÃO' and b.upper() and c.upper() and d.upper()=='SIM' or b.upper() and c.upper()=='NÃO' and a.upper() and d.upper() and e.upper()=='SIM':
    print("Cúmplice ")
elif a.upper() and b.upper() and c.upper() and d.upper() and e.upper()=='SIM':
    print("Assassino")
else:
    print("LIBERADO")
