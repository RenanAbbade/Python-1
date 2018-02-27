'''Exercicio 03 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
#ENTRADA
data = input("Digite uma data no formato aaaammdd ")

#PROCESSAMENTO
dia = int(data[6:8])
mes = int(data[4:6])
ano = int(data[0:4])

#SAIDA
if data[4:6]=='01':
    print(dia,"/","Janeiro","/",ano)
elif data[4:6]=='02':
    print(dia,"/","Fevereiro","/",ano)
elif data[4:6]=='03':
    print(dia,"/","Março","/",ano)
elif data[4:6]=='04':
    print(dia,"/","Abril","/",ano)
elif data[4:6]=='05':
    print(dia,"/","Maio","/",ano)
elif data[4:6]=='06':
    print(dia,"/","Junho","/",ano)
elif data[4:6]=='07':
    print(dia,"/","Julho","/",ano)
elif data[4:6]=='08':
    print(dia,"/","Agosto","/",ano)
elif data[4:6]=='09':
    print(dia,"/","Setembro","/",ano)
elif data[4:6]=='10':
    print(dia,"/","Outubro","/",ano)
elif data[4:6]=='11':
    print(dia,"/","Novembro","/",ano)
elif data[4:6] == '12':
    print(dia, "/", "Dezembro", "/", ano)