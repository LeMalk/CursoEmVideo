# Exercício 011

# Faça um programa que leia a largura e altura em metros
# calcule sua área e a quantidade de tinta para pintá-la
# sabendo que cada litro de tina pinta uma área de 2m²

alt = float(input('Coloque a altura da parede: '))
lag = float(input('Coloque a largura da parede: '))
area = alt * lag
# Decidi por colocar a tinta como variável para mudar o rendimento caso consiga uma tinta que cubra mais.
tint = 2.0

print('Para uma parede de área: {}. Você vai precisar de {} litros de tinta'.format(area, area/tint))
