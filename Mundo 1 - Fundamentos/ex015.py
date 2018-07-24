# Exercício 015

# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60,00 por dia e R$ 0,15 por KM rodado.

dias = float(input('Quantos dias o carro está alugado? '))
km = float(input('Quantos kilometros foram rodados? '))

diap = dias*60
kmp = km*0.15

print('O preço total é {:.2f}.\nVocê está pagando {:.2f} por dias alugados.\nVocê está pagando {:.2f} por Km rodado.'.format(diap + kmp, diap, kmp))
