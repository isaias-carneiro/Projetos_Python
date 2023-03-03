# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
frase = str(input('Qual o seu nome completo? ')).strip()
print('maiúscolo !')
print(frase.upper())
print('minuscolo ! {}'.format(frase.lower()))
print('total de letras com os espaços no inicio e fim !')
print(len(frase) - frase.count(' '))
print('total de caracteres sem os espaços !')
print(len(frase.strip()))
print('dividida em palavras !')
print(frase.split())
print('seu primeiro nome tem {}'.format(frase.find(' ')))
sep = frase.split()
print('seu segundo nome é {} e ele tem {} letras'.format(sep[1], len(sep[1])))
