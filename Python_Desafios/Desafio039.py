# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''idade = int(input('Qual a sua idade: '))
status = str(input(''''''Qual a sua relação com as forças armadas?
[s] para sim já compri meu tempo de serviço
[n] para não me alistei
[es] para estou servindo\n ''''''))
if idade < 17:
    tempo = 17 - idade
    print('Você ainda não pode se alistar, faltam {} ano(s)'.format(tempo))
elif 17 <= idade <= 18: # elif idade >= 17 and idade <= 18
       print('Você esta dentro do periodo correto para o alistamento')
elif idade > 18 and status == 'n':
    tempo = idade - 18
    print('Você perdeo o periodo de alistamento, esta atrazado em {} ano(s)'.format(tempo))
elif idade > 18 and status == 's':
    print('Parabens guerreiro e obrigado por ter servido a patria!')
elif idade > 18 and status == 'es':
    print('Muito bem soudado!')
else:
    print('Dados incorreto!')'''

from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('você de ve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
