# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# variaveis
termo = int(input('Informe o termo da PA: '))
razao = int(input('Iforme a razão da PA: '))

# calculo matematico de uma PA
decimo = termo + (10 - 1) * razao

# criando o laço < o termo é onde começa e a razão é o intervalo >
for conte in range(termo, decimo + razao, razao):
    print(conte, end=' ')
print('Fim')
