# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fra = str(input('Digite uma frase: ')).strip().upper()
print('nesta frase a letra A aparece {} veses'.format(fra.count('A')))
print('o primeiro A, apareci na posição {}'.format(fra.upper().find('A')+1))# +1 para disconciderar o '0' na contagem
print('a ultima vez que aparece a letra A é na posição {}'.format(fra.rfind('A')+1))# nesse caso não é necessario
# o upper, pois ja tem ele no comesso do programa
