# Exercício 029
#
# Escreva um Programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre que ele foi multado.
# A multa vale R$ 7,00 por cada Km acima do limite.

vel = int(input('Insira a velocidade medida: '))

if vel > 80:
    print('Você foi multado!')
    multa = float(vel - 80) * 7
    print('O valor da multa é: R${:.2f}'.format(multa))
else:
    print('Velocidade dentro do limite.')
