# Crie um programa que faça o computador pençar em um número inteiro entra 0 e 5,
# e peça para o usuario adivinhar qual foi o número escolhido pelo pc. O programa de ve escrever na tela se você ganhou ou perdeu
import random
from time import sleep # biblioteca de tempo
n = int(input('Em que número estou pensando entre 0 e 5? '))
r = random.randint(0, 5)
print('Processando...')
sleep(2) # cria uma espera
if n == r:
    print('Você ganhou, parabens!')
else:
    print('Você perdeu, eu pensei em {}'.format(r))
