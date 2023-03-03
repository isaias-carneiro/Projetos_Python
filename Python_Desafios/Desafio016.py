# Crie um programa que leia pelo teclado um número real qualquer e mostre sua parte inteira
import math
n = float(input('Digite um número Real: '))
print('O valor digitado foi {}, sua porção inteira é {}'.format(n, math.trunc(n))) # opção 1

from math import trunc
m = float(input('de um valor Real: '))
print('a sua parte inteira é {}'.format(trunc(m))) # opção 2

num = float(input('de um número real: '))
print('A parte inteira desse valor é {}'.format(int(num))) # opção 3

