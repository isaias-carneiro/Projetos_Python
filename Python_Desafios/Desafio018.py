# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
an = float(input('qual é o ângulo? '))
s = math.sin(math.radians(an))
print('O ângulo {} tem o seno {:.2f}'.format(an, s))
c = math.cos(math.radians(an))
print('O ângulo {} tem o cosseno {:.2f}'.format(an, c))
t = math.tan(math.radians(an))
print('O ângulo {} tem a tangente {:.2f}'.format(an, t))
print('Opção 2')
from math import radians, sin, cos, tan
ang = float(input('qual é o ângulo? '))
se = sin(radians(ang))
print('O ângulo {} tem o seno {:.2f}'.format(ang, se))
co = cos(radians(ang))
print('O ângulo {} tem o cosseno {:.2f}'.format(ang, co))
ta = tan(radians(ang))
print('O ângulo {} tem a tangente {:.2f}'.format(ang, ta))
