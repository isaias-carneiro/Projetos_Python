#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n1 > n2 and n1 > n3:
    maior = n3
print(f'Menor valor é {menor} e o maior é {maior}')
