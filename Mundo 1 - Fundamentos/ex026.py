# Exercício 26
#
# Faça um programa que leia uma frase pelo teclado,
# mostre quantas vezes aparece a letra A,
# em que posição ela aparece pela primeira vez
# e em que posição ela aparece pela última vez.

frase = str(input('Insira um frase qualquer: ')).strip().lower()

print('Sua frase tem {} letra(s) A'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na pocição {}'.format(frase.rfind('a')+1))
print(len(frase))
