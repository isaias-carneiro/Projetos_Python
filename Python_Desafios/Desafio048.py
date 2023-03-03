# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0 # acumulador de números
cont = 0 # contador de números
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1 # é o mesmo que <cont = cont + 1>
print(soma)
print(cont)
