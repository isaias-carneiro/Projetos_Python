# Elabore um programa que calcule o valor a ser pago por um preço, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
preço = float(input('Valor do preço: R$ '))
print()
print('''Opções de pagamento
[1] Avista dinheiro/cheque
[2] Avista no Debito
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print()
opção = int(input('Escolha uma opção a cima: '))
print()
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('A sua compra ficou dividida 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    x = int(input('Em quantas vezes quer dividir: '))
    parcela = total / x
    print()
    print('A sua compra ficou dividida em {}x de R$ {:.2f} com juros'.format(x, parcela))
print()
print('A sua compra de R$ {:.2f}, fica R$ {:.2f}'.format(preço, total))
