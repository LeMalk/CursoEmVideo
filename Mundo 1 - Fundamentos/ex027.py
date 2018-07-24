# Exercício 027
#
# Faça um programa que leia o nome completo
#  de uma pessoa, mostrando em seguida o primeiro
#  e o último nome separadamente.

nome = str(input('Insira seu nome: '))

nomdiv = nome.split()

print('Olá {}'.format(nomdiv[0]))
print('Seu primeiro nome é {}'.format(nomdiv[0]))
print('Seu último nome é {}'.format(nomdiv[-1]))
