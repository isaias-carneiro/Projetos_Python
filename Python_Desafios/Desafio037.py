# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um número inteiro qualquer: "))
print('''Escolha uma opção para conversão
[1] para Binario
[2] para Octal
[3] para Exadecimal''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido em Binario é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em Exadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opição invalida!')
