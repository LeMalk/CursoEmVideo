# Exercício 035
#
# Desenvolva um programa que leia
# o comprimento de três retas e diga
#  ao usuário se elas podem ou não
# formar um triângulo.

r1 = int(input('Insira o comprimento da primera reta: '))
r2 = int(input('Insira o comprimento da segunda reta: '))
r3 = int(input('Insira o comprimento da terceira reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
