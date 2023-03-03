# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada
import random
n1 = input('Aluno: ')
n2 = input('Aluno: ')
n3 = input('Aluno: ')
n4 = input('Aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista) # shuffle - embaralhar da lista
print('A ordem sera')
print(lista)
