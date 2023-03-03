# Faça um programa que leia um número inteiro e moste na tela o seu sucessor e seu antecessor.
n = int(input("digite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {},\né certo que o seu antecessor é {}\ne seu sucessor é {}". format(n, a, s)) # opção 1
print(' ')
m = int(input('Dé um valor: '))
print('o antecessor de {} é {} e o sucessor é {}'.format(m, (m-1), (m+1))) # opção 2
