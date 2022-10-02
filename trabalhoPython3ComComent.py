#2. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar

numero = float(input('Digite um número : '))

if numero % 2 == 0:
    print(f'O número que você digitou é PAR, número digitado : {numero}')
else:
    print(f'O número que você digitou é ÍMPAR, número digitado : {numero}')
    #aqui tambem usando o if e else