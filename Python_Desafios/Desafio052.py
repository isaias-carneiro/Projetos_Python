# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# contador / variavel
total = 0
num = int(input('Digite um número: '))

# criando o laço
for c in range(1, num + 1):

    # criando a condição < se num resto da divisão por c for igual a 0 >
    if num % c == 0:
        total += 1 # então total sera += 1

    else: # se não imprima c
        print(c, end=' ')
print('O número {}, foi dividido {} vezes'.format(num, total))

# se total for igual 2, ele é primo
if total == 2:
    print('Por isso ele é Primo')

else: # se não for igual a 2 ele não é primo
    print('Por isso ele não é Primo')
