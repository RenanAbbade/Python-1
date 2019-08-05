'''Considere o problema de conversão de temperatura. Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de Fahrenheit para Celsius (O usuário deve digitar F) e de Celsius para Fahrenheit
(O usuário deve digitar C). Para a construção do programa você deve escrever as seguintes funções:
(a). exibeMsg() -  apenas exibe uma msg para o usuário dizendo o que o programa faz e informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não retorno.
(b). getConvertTo() - a função não tem parâmetro de entrada e retorna “F” ou “C”
(c). exibeFahrenheitTOCelsius(start, end) – essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Celsius
(d). exibeCelsiusTOFahrenheit(start, end) – essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Fahrenheit
C -> F -> F = C*1.8+32
F -> C -> C = (F-32)/1.8
.'''
import time
#%% ----------------------- Explica o programa --------------------------------
def exibeMsg():
    print('Esse programa faz a conversão de temperatura, Fahrenheit para Celsius ou Celsius Para Fahrenheit')
    return
#%% ----------------------- Pergunta Qual opção o usuario quer ----------------
def getConvertTo():
    escolha = input('Para converter de Fahrenheit para Celsiu digite "F". Para converter de Celsius Para Fahrenheit Digite C: ')
    return escolha
#%% ----------------------- Converte fahrenheit para celsius-------------------
def exibeFahrenheitTOCelsius():
    start = float(input('Digite a temperatura em fahrenheit para ser convertida para Celsius: '))
    end = (start - 32) / 1.8
    return end
#%% ----------------------- Converte celsius para fahrenheit-------------------
def exibeCelsiusTOFahrenheit():
    start = float(input('Digite a temperatura em Celsius para ser convertida para fahrenheit : '))
    end = (start * 1.8) + 32
    return end
#%% ----------------------- Saida do programa ---------------------------------
exibeMsg()
print('\n\n')
time.sleep(1)
if getConvertTo() == 'f'.upper():
    print('Processando  ..')
    time.sleep(1)
    print('Resultado é: {:.0f}'.format(exibeFahrenheitTOCelsius()),"Cº")
else:
    print('Processando  ..')
    time.sleep(1)
    print('Resultado é: {:.0f}'.format(exibeCelsiusTOFahrenheit()),"Fº")




