#2João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
#multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
#de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
#os dados do programa com as mensagens adequadas.

pesoPeixe = float(input('Digite o KG do peixe pescado [Ex = 78.5] : '))

if pesoPeixe > 50:
    multa = 4 * (pesoPeixe - 50)
    kgUltrapassado = pesoPeixe - 50
    print(f'Quantidade de KG excedente {kgUltrapassado} KG\nCom isso sua multa será de : R${multa} ')
else:
    print(f'Tudo certo, {pesoPeixe} KG')

#aqui tambem usando o if e else com os calculos em suas respectivas variaveis  sendo que o if ja
#calculado a multa e o else como ele nao é multado segue como saida TUDO CERTO