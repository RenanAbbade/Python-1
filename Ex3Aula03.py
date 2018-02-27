'''
#RENAN ABBADE
18/08/2017

print("{0:.2f}".format(a))
13.95
print(10 % 2)
'''

#ENTRADA

tarefa = float(input("Quantos segundos durou a tarefa? "))


horas = tarefa/3600
resto1 = (tarefa%3600)
minutos = resto1/60
resto2 = (resto1%60)
segundos = resto2

#SAIDA

print("O tempo levado foi ", "{0:.0f}".format(horas), ":", "{0:.0f}".format(minutos),":","{0:.0f}".format(segundos))

