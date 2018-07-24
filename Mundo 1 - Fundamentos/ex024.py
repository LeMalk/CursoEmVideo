# Exercício 24

# Crie um programa que leia o nome de uma cidade
# e diga se ela começa com "Santo".

import sys
print(sys.version)

cidade = str(input('Insira o nome da sua cidade: ')).strip()

cidiv = cidade.split()

if('Santo' in cidiv[0].capitalize()):
    print('A cidade {} começa com Santo no nome.'.format(cidade))
else:
    print('A cidade {} não começa com Santo no nome'.format(cidade))
