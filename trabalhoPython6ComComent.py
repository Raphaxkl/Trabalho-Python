#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input("\nDigite um número: "))

if (num == round(num)):

    print(int(num),"é um número inteiro!")

else:

    print(num,"é um número decimal!")
    #aqui a entrada de dados é em float caso o usuario digite o numero com ponto flutuante é decimal
    # caso ele digite numeros inteiros o if age  e printa e numero inteiro