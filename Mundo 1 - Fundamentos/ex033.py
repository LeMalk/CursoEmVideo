# Exercício 033
#
# Faça um programa que leia três números
# e mostre qual o maior e qual o menor.

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
num3 = float(input('Insira o terceiro número: '))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if  num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

print('O maior é {} e o menor é {}'.format(maior, menor))
