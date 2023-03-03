# Faça um algoritmo que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pintar uma area de 2m²
#larg = float(input('Largura da parede: '))
#alt = float(input('Altura da parede: '))
#area = larg * alt
#print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, area))
#tinta = area / 2
#print('Você ira precisar de {:.2f}l de tita para essa parede.'.format(tinta))

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