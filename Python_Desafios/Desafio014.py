# Escreva um programa que converta uma temperatura de Cº para Fº
import emoji
c = float(input('Informe a temperatura em Cº '))
f = ((9 * c)/5)+32 # formula de converção Cº para Fº. tambem da certo sem os parenteses
print('A temperatura de {:.1f}Cº, convertida para Fº é {:.1f}Fº!'.format(c, f))
print(emoji.emojize(':man_surfing:'))
