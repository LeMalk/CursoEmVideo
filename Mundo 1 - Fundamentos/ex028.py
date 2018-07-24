# Exercício 028

# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computado.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = random.randrange(1, 6)
tent = int(input('Insira um número de 1 a 5: '))

if num == tent:
    print('Parabéns, você acertou')
else:
    print('Que pena você errou, eu tinha pensado no nº {}'.format(num))
