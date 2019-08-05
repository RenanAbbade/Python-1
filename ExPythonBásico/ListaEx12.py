'''
Exercicio 12 lista de exercicios

Author:Renan Abbade 31782299 - 06/09/2017'''

#ENTRADA
pressao_desejada = int(input("Digite a pressão desejada pelo motorista "))
pressao_lida = int(input("Digite a pressão lida pela bomba "))

#PROCESSAMENTO
if pressao_desejada>=1 and pressao_desejada<=40 and pressao_lida>=1 and pressao_lida<=40:
    print("A diferença entre a pressão desejada e a pressão lida será de ",pressao_desejada-pressao_lida)
else:
    print("Os números digitados devem estar entre 1 e 40")