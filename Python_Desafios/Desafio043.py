# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Com uma altura de {:.2f}m e pesando {:.2f}kg, seu IMC é {:.2f}!'.format(peso, altura, imc))
if imc < 18.5:
    print('Você esta Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você esta no Peso Ideal')
elif 25 > imc <= 30:
    print('Você esta com Sobrepeso')
elif 30 > imc <= 40:
    print('você esta com Obesidade')
else:
    print('Você esta com Obesidade Morbida')
