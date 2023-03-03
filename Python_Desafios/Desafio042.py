# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a seegunda reta: '))
r3 = float(input('informe a ultima reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um TRIÂNGULO', end=' ')
    if r1 == r2 == r3:
        print('EQUILTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÒSCELES!')
else:
    print('Impocivel se formar qualquer Triângo!')
