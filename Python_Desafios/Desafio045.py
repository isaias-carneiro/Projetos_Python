# Jokenpo
# import random
# print()
# print('\033[1;41m-\033[m' * 80)
# print()
# joq = str(input('   \033[1;34mEscolha: (pe) para Pedra, (pe) para Papel ou (te) para Tesoura\033[m\n   '))
# lista = ['pe', 'pa', 'te']
# resul = random.choice(lista)
# if joq == 'pa' and resul == 'te':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m, você \033[1;31mPERDEU !\033[m'.format(joq, resul))
# elif joq == 'pe' and resul == 'te':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m. você \033[1;32mGANHOU !\033[m'.format(joq, resul))
# elif joq == 'pa' and resul == 'pe':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m. você \033[1;32mGANHOU !\033[m'.format(joq, resul))
# elif joq == 'te' and resul == 'pe':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m. você \033[1;31mPERDEU !\033[m'.format(joq, resul))
# elif joq == 'pe' and resul == 'pa':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m. você \033[1;31mPERDEU !\033[m'.format(joq, resul))
# elif joq == 'te' and resul == 'pa':
#    print('Você jogou \033[4;36m{}\033[m, eu joguei \033[4;36m{}\033[m. você \033[1;32mGANHOU !\033[m'.format(joq, resul))
# else:
#    print('\033[1;33mDeu Empate\033[m')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Opições
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('Computador Jogou {}'.format(itens[computador])) # ler-se, -itens na posição computador-
print('Jogador jogou {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VEMCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
