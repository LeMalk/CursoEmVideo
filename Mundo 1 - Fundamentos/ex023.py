# Exercício 23
# Faça um programa que leia um número de 0
# a 9999 e mostre na tela cada um dos dígitos separados

num = str(input('Insira um número de 0 a 9999: '))

if (len(num)==4):
    print("""Seu número tem:
    Unidade: {}
    Dezenas: {}
    Centenas: {}
    Milhares: {}""".format(num[3], num[2], num[1], num[0]))
elif(len(num)==3):
    print("""Seu número tem:
    Unidade: {}
    Dezenas: {}
    Centenas: {}""".format(num[2], num[1], num[0]))
elif(len(num)==2):
    print("""Seu número tem:
    Unidade: {}
    Dezenas: {}""".format(num[1], num[0]))
else:
    print("""Seu número tem:
    Unidade: {}""".format(num))
