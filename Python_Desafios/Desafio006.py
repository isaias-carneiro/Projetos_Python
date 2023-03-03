# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2) # raiz quadrada
p = pow(n, 2) # potencia
print('O dobro de {} é {}\no triplo é {}\ne a raiz é {:.1f}\na potencia é {}'.format(n, d, t, r, p)) # opção 1
print('O dobro é {}\nO triplo é {}\nA raiz é {}\nE a potencia é {}'.format((n*2), (n*3), pow(n, (1/2)), pow(n, 2))) # opção 2
