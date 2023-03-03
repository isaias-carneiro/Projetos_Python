#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nom = str(input('Qual o seu nome? ')).strip()
print('seo nome tem Silva? {}'.format('SILVA' in nom.upper())) # in é um operador e não uma função do pythom
