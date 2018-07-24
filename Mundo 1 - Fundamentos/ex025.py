# Exércio 25
#
# Crie um Programa que leia o nome de uma pessoa
# e diga se ela tem "Silva" no nome

nome = str(input('Insira seu nome: '))

if('silva' in nome.lower()):
   print('Você tem Silva no nome')
else:
   print('Você não tem Silva no nome')