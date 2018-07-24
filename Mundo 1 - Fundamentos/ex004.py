# Exercício 004
# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo
# e todas as informações possíveis sobre ela

algo = input('Digite algo: ')

print('O tipo primitivo desse valor "{}" é: {} \n'.format(algo, type(algo)))
print('"{}" Só tem espaço? {}'.format(algo, algo.isspace()))
print('"{}" É um número? {}'.format(algo, algo.isnumeric()))
print('"{}" É alfabético? {}'.format(algo, algo.isalpha()))
print('"{}" É alfanumérico? {}'.format(algo, algo.isalnum()))
print('"{}" Está em maiúsculas? {}'.format(algo, algo.isupper()))
print('"{}" Está em minúsculas? {}'.format(algo, algo.islower()))
print('"{}" Está capitalizado? {}'.format(algo, algo.istitle()))
