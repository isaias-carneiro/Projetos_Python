# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Escolha a tabuada que você deseja: '))
for c in range(1, 11):
    print('{:>40}'.format('{} x {:2} = {:3}'.format(num, c, num * c)))
