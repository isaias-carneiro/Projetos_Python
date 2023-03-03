# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode eceder 30% do salario ou então o emprestimo serar negado
print('\033[1;31m-\033[m' * 60)
casa = float(input('Quanto custa o imovel?\n '))
salario = float(input('Qual o seu salario?\n '))
anos = int(input('Em quantas parcela deseja?\n '))
parcela = casa / (anos * 12) #
print('o valor daparcela sera de {:.2f}'.format(parcela))
if parcela > (salario * 30) / 100:
    print("seu emprestimo foi negado")
else:
    print('seu emprestimo foi aprovado')

# casa = float(input('Quanto custa o imovel?\n '))
# salario = float(input('Qual o seu salario?\n '))
# anos = int(input('Em quantas parcela deseja?\n '))
# parcela = casa / (anos * 12)
# minimo = salario * 30 / 100