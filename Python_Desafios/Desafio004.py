# Faça um programa que leia algo na tela e mostre o seu tipo primitivo e todas as informações possiveis sobre ele.
a = input('Digite algo: ')  # input sempre retorna um tipo primitivo string
print('O tipo primitivo desse valor é ', type(a))  # tipo
print("Só tem espaços? ", a.isspace())  # 'a' é um objeto, sempre que tiver '.is...()' antes do objeto ele é um metodo
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiúscula? ', a.isupper())
print('Esta em minuscula? ', a.islower())
print("esta capitalizada? ", a.istitle()) # quando uma palavra tem letras maiúsculas e minusculas
# tipos primitivos - int(inteiro), float(números reais), bool(verdadeiro e falso), str(string)
