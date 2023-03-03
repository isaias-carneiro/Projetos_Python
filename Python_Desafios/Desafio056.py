#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#  a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
totah = 0
somaidade = 0
totalm = 0
totalml = 0
nomevelho = ''
maioridade = 0

for l in range(1, 5):
    print('=============== {}º ============'.format(l))
    print()
    nome = str(input('Qual o seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual o sexo (M , F): '))

    somaidade += idade

    if l and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 0:
        totalm += 1
    if sexo in 'Mm' and idade > 0:
        totah += 1
    if sexo in 'Ff' and idade < 20:
        totalml += 1
media = somaidade / 4
print()
print('Media de idade do grupo é de {}'.format(media))
print('O número de mulheres com menos de 20 anos é de {}'.format(totalml))
print('O homem mais velho do grupo é {}'.format(nomevelho))
