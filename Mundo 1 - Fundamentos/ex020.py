# Exercício 020

# O mesmo professor quer sortear a ordem
# de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos 4
# alunos e mostre a ordem sorteada

from random import shuffle

alunos = ['aluno1', 'aluno2', 'aluno3', 'aluno4']

# shuffle embaralha no local e não retorna resultado, necessitando de uma variável
# ordem = alunos[:]
shuffle(alunos)
# nesse caso como não precisamos manter a ordem do array a variável extra é dispesável.
print('A ordem sorteada é: {}'.format(alunos))
