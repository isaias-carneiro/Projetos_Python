# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
nota = (n1 + n2 + n3) / 3
if nota >= 7:
    print('Você Passou com media {:.1f}'.format(nota))
elif 5 <= nota < 7:
    print('Você não atingio a media para passar. Sua media foi {:.1f}, esta de recuperação'.format(nota))
else:
    print('Você foi reprovado, com nota de {:.1f}'.format(nota))