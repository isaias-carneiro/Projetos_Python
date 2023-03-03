#  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('de um comprimento de reta: '))
r2 = float(input('mais um comprimento de reta: '))
r3 = float(input('e mais outro comprimento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # fomula matematica para formar um triângulo
    print('Os seguimentos acima podem formar um TRIÂNGULO')
else:
    print('esses seguimentos não formam um TRIÂNGULO!')
