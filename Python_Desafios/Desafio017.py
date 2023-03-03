# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
co = float(input('Qual é cateto oposto: '))
ca = float(input('Qual é o cateto adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** (1/2) # Formula matematica para calculo da hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(h)) # opção 1
print('=' * 30)
import math
o = float(input('cateto oposto: '))
a = float(input('cateto adjacente: '))
hi = math.hypot(o, a) # hypot - hipotenusa
print('A hipotenusa é {:.2f}'.format(hi)) # opção 2