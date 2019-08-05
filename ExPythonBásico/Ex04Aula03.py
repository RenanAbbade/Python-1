#ENTRADA

ano = int(input("Digite o seu ano de nascimento "))
mes = int(input("Digite o seu mes de nascimento "))
dia = int(input("Digite o seu dia de nascimento "))

#1 Anos = 31557600 Segundos
#1 Meses = 2629800 Segundos
#1 Dias = 86400 Segundos

vida = 2017 - ano
seg_ano = vida*31557600

meses = 12 - mes
seg_mes = meses*2629800

dias = 31-dia
seg_dia = dias*86400

print("A idade aproximada em segundos será ", seg_ano+seg_dia+seg_mes)

