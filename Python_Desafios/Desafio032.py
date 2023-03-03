# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Escolha um ano para saber se ele é bisiesto: '))
if ano == 0:
    ano = date.today().year # pega ona atual da configuração da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:# != diferente de. or ou.<se ano resto da divisão por 4 for igual a 0 e ano resto da divisão por 100 for diferente de 0 ou ano resto da divisão por 400 for igual a 0>
    print('esse ano {} é BISIESTO!'.format(ano))
else:
    print('esse ano {} NÂO é BISIESTO!'.format(ano))
