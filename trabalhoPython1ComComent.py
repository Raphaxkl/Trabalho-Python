#1. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
#peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7

sexo = input('Digite seu sexo para saber seu peso ideal [M / F]  : ').upper().strip()
altura = float(input('Digite sua Altura [ex = 1.86]  : '))

if sexo == 'M':
    pesoIdealHomem = (72.7 * altura ) - 58
    print(f'Seu peso ideal, considerando o sexo masculino é : {pesoIdealHomem:.2f}')
elif sexo == 'F':
    pesoIdealFeminino = (62.1 * altura) - 44.7
    print(f'Seu peso ideal, considerando o sexo feminino é : {pesoIdealFeminino:.2f}')

    #esta tarefa basicamente eu usei o if e else para separar M de n e para onde o usuario indicar
    #sera direcionado para o respectivo calculo atribuido as variaveis