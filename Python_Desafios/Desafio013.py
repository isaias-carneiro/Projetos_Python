# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de almento
import emoji
t = float(input('Qual é o salario atual? R$ '))
p = float(input('Qual sera a porcentagem adicionada? %'))
l = t + (t * p / 100)
print('O novo salario com {}% de almento, passarar a ser de R$ {:.2f}'.format(p, l), end=' ')
print(emoji.emojize(':man_student:'))
