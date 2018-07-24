# Exercício 008

# Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros

n1 = float(input('Insira a quantidade de metros: '))

print('Você inseriu {} metros.\nEquivale a {:.1f} centímetros.\nEquivale a {:.1f} milímetros.'.format(n1, n1*100, n1*1000))
