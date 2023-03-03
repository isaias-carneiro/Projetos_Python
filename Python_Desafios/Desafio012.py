# Faça um programa que leia o preço de um preço e mostre seu novo preço com 5% de desconto
p = float(input('Qual é o preço do preço? R$ '))
n = p - (p * 5 / 100)
print('O novo preço com 5% de desconto é R$ {:.2f}'.format(n))
