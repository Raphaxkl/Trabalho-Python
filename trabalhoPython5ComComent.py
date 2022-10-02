#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
#dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.


ganhoPorHoraTrabalhada = float(input('Digite o quanto você ganha por hora trabalhada :R$ '))
numeroDeHorasTrabalhada = float(input('Digite a quantidade de horas trabalhadas : '))
diasTrabalhouNoMes = int(input('Quantos dias trabalhou no mês : '))

salario = diasTrabalhouNoMes * (ganhoPorHoraTrabalhada * numeroDeHorasTrabalhada)

ir = salario - (salario * 11/100)
sindicato = salario - (salario * 5/100)
inss = salario - (salario * 8/100)
salarioLiquido =  salario - ((salario - ir) + (salario - sindicato) + (salario - inss))

print(f'Salário bruto : {salario:.2f}\nInss(8%) : {inss:.2f}\nsindicato(5%) : {sindicato:.2f}\nIR(11%) : {ir:.2f}'
      f'\nsalário liquido : {salarioLiquido:.2f}')
#aqui foi mais complicado e demorei
#mas basicamente criei variaveis e anexando as entrada de dados
#criei uma var salario ccalculando
#e outras var tambem fazendo os calculos e ao final o print