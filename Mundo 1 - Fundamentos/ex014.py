# Exercício 014

# Escreva um programa que converta uma temperatura digitada em Cº para Fº.

temp = int(input('Insira um temperatura em Cº: '))

# Fórmula de conversão
# TC/5 = (TF-32)/9

uc = temp/5
tf = uc*9+32

print('O equivalente de {} Cº é {} Fº'.format(temp, tf))
