# Exercício 010

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

din = float(input('Coloque quanto diheiro você tem: '))
dol = 3.27

print('Você pode comprar {:.2f} dólares'.format(din/dol))
