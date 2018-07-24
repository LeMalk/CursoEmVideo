# Exercício 034
#
# Escreva um programa que pergunte o salário de
# um funcionário e calcule o seu aumento.
# Para salários acima de R$1250,00 o aumento é
# de 10%.
# Para salários inferiores a R$1250,00 o aumento
# é de 15%.

sal = float(input('Insira o salário: '))

if sal > 1250:
    print('Seu novo salário é: R${}'.format(sal + sal * 0.10))
else:
    print('Seu novo salário é: R${}'.format(sal + sal * 0.15))
