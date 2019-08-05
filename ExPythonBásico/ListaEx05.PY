'''Exercicio 05 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''
#ENTRADA
num_apartamentos = float(input("Digite o número de apartamenteos do hotel"))
ocupados = float(input("Digite o número dos apartamentos que foram ocupados "))
diaria = float(input("Digite o valor da diária para o fim de semana completo "))

#PROCESSAMENTO
diaria_desconto = diaria*0.85

if num_apartamentos/ocupados==1:
    '''Ocupação atinge 100%'''
    print("Ocupação atinge 100%, valor total arrecadado é",diaria_desconto*ocupados,"R$")
    print("O valor que o hotel deixara de acumular em virtude da promoção será ",(diaria*ocupados)-(diaria_desconto*ocupados,"R$"))
elif num_apartamentos*0.70==ocupados:
        print("Ocupação de 70%, valor arrecadado é", diaria_desconto*ocupados,"R$")
else:
    print("Valor promocional desta diaria arrecadado para o fim de semana será ", diaria_desconto*ocupados,"R$")