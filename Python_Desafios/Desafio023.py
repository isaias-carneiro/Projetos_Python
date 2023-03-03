# Fça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''num = int(input('digite um número: '))
n = str(num) # forma com string (não recomendado para todos os números) usa o fatiamento de str
print('unidade é {}'.format(n[3]))
print('dezena  é {}'.format(n[2]))
print('centena é {}'.format(n[1]))
print('milhar  é {}'.format(n[0]))
print('')
print('='*20)
print('')
nu = int(input('informe um número: '))
unidade = nu // 1 % 10
dezena = nu // 10 % 10
centena = nu // 100 % 10
milhar = nu // 1000 % 10 # Formula matematica para fatiar números
print('a unidede é {}'.format(unidade))
print('a dezena  é {}'.format(dezena))
print('a centena é {}'.format(centena))
print('a milhar  é {}'.format(milhar)'''
import PySimpleGUI as sg

WIN_V = 50
WIN_H = 70

layout = [
    [sg.Text('Determine um valor numerico'), sg.Int(Input())],
    [sg.Text(' ')]
]

window = sg.Window()
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED():
        break

window.clese()
