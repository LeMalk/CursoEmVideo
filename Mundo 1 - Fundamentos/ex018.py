# Exercício 018

# Faça um programa que leia um âgulo qualquer
# e mostre na tela o valor do seno, cosseno e
# a tangente desse ângulo.

from math import cos, sin, tan

ang = float(input('Insira um ângulo: '))
print(
    'O seno deste ângulo é {:.2f}\nO cosseno desse ângulo é {:.2f}\n A tangente desse ângulo é {:.2f}'.format(sin(ang),
                                                                                                              cos(ang),
                                                                                                              tan(ang)))
