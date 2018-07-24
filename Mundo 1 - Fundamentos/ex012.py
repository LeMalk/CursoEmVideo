# Exercício 012

# Faça um algoritmo que leia um preço de um produto
# e mostre seu novo preço com 5% de desconto

prec = float(input('Insira o preço do produto: '))

print('O preço com desconto é {:.2f}'.format(prec-prec*0.05))
