# Exercício 009

# Faça um programa que leia um número inteiro qualquer
# e mostre na tela sua tabuada

n1 = int(input('Insira um número: '))
x = 0

for x in range(11):
    print('{}x{}={}'.format(n1, x, n1*x))

