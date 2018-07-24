# Exercício 031
#
# Desenvolva um programa que pergunte a distância de
# uma viagem em Km. Calcule o preço da passagem, cob-
# rando R$0,50 por viagens até 200Km e R$0,45 para v-
# iagens maiores.

preco1 = float(0.5)
preco2 = float(0.45)

dist = float(input('Insira a distância em Km da sua viagem: '))

if dist <= 200:
    print('Sua viagem vai custar: R${:.2f}'.format(dist*preco1))
else:
    print('Sua viagem vai custar: R${:.2f}'.format(dist*preco2))
