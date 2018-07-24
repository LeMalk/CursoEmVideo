# Exercício 019

# Um professor quer sortear um de seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele
# lendo o nome dos quatro alunos e escrevendo o nome do
# aluno sorteado.

from random import choice

alunos = ['aluno1','aluno2','aluno3','aluno4']

print('O aluno sorteado é: {}'.format(choice(alunos)))
