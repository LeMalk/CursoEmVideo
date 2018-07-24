# Exercício 016

# Crie um programa que leia um número Real
# qualquer e mostre na tela sua porção inteira

from math import trunc

num = float(input('Insira um número real: '))
print('A parte inteira é: {}'.format(trunc(num)))
