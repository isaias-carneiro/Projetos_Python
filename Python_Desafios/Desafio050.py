#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.

# contador / variavel
s = 0

# criando o laço de 1 a 6 repetições
for c in range(1, 7):

    # requisitando o valor de entrada
    n = int(input('gigite um número: '))

    # incerindo a condição para o calculo
    if n % 2 == 0:
        s += n

# imprimindo o resultado final
print('asoma dos pares é de {}'.format(s))
