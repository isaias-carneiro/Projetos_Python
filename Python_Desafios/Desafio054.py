#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#  maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
menor = 0
maior = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoa)))
    idade = atual - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo são {} pessoas Menor de Idade!'.format(menor))

print('Ao todo são {} pessoas maior de Idade!'.format(maior))
