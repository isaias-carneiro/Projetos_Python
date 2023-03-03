#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#  cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distância = float(input('Quantos km você vai viajar? '))
if distância <= 200:
    print('O valor da sua passagem é R$ {}'.format(distância * 0.50))
else:
    print('O valor de km ecedente é {}'.format(distância * 0.45)) # 1ª opção
print(' ')

d = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a fazer uma viagem de {}km.'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O preço da sua passagem sera de R$ {:.2f}'.format(preço)) # 2ª opção
print(' ')

a = float(input('Qual a distancia de sua viagem? '))
print('Você ira fazer uma viagem de km {}'.format(a))
pre = a * 0.50 if a <= 200 else a * 0.45
print('A sua passagem vai custar R$ {:.2f}'.format(pre)) # 3ª opção
