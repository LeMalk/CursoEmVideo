# Exercício 017

# Faça um programa que leia o comprimento de um cateto oposto
# e do cateto adjacente de um triângulo retângulo e mostre o
# comprimento da hipotenusa

from math import hypot

cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))

print('A hipotenusa é: {:.2f}'.format(hypot(cato, cata)))
