#  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Qual é a sua cidade? ')).strip() # strip no final do linha para eliminar qualquer espaço futuro
print(cidade[:5].upper() == 'SANTO') # [:5] vai ler do 0 ate a letra 5, .upper() vai jogar tudo pra maiusculo e procurar 'SANTO' em maiusculo