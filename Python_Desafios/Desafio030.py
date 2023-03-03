# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número: '))
resp = num % 2 # resto da divisão por dois retorna '0' ou '1'
if resp == 0:
    print('esse numero é PAR')
else:
    print('esse numero é IMPAR')
