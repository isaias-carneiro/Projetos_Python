# Escreva um programa que leia a velocidade de um caro.
# se ele ultrapassar 80km/h, mostre uma menssagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima dolimite
velocidade = float(input('Qual éa velocidade do carro? '))
if velocidade > 80:
    print('Você foi MULTADO! Ultrapassou o limite de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você vai ter que pagar R$ {:.2f} de multa'.format(multa))
print('Tenha um bom dia e dirija com cuidado!')
