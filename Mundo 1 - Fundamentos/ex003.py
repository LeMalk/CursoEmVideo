# Exercício 003

# Crie um script de Python que leia
# dois números e mostre a soma entre eles

print('====== DESAFIO 03 ======')

a = input('Qual o primeiro número? ')
b = input('Qual o segundo número? ')

soma = int(a) + int(b)

# print('A soma é: ', soma)

print('A soma entre {0} e {1} é igual a {2}'.format(a, b, soma))
