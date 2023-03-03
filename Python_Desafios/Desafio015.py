# Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.
km = float(input('Quantos quilometros rodado? '))
d = int(input('Quantos dias? '))
v = (d * 60) + (km * 0.15)
print('Você pagarar R$ {:.2f}'.format(v))
