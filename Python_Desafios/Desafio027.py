#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Qual o seo nome? ')).strip()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('o seu ultimo nome   é {}'.format(n[len(n)-1])) # nesse caso é nescessario fatiar a frase para pedir a contagem
