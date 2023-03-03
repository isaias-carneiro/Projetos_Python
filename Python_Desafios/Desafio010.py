# Crie um programa que diga quantos dolares você pode comprar com o dinheiro da sua carteira
# levando em conta que 1 U$ equivale a 3.27 R$
crt = float(input('Quanto vc tem na carteira? R$'))
dol = crt / 3.27
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(crt, dol))
