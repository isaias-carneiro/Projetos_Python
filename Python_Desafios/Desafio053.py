# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase =str(input('Digite uma frase: '))

palavra = frase.split()
junto=''.join(palavra)
inverso= ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('A frase não é um Palindromo')
