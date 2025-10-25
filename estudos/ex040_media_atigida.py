# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre de 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 OU superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunta nota: '))
media = (n1 + n2) / 2
print('Sua primeira nota é {:.1F}, e sua segunda nota é {:.1F}, então sua média foi de {:.1F}'.format(n1, n2, media))
if media <= 5:
    print('Você está REPROVADO!')
elif media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print('Você está APROVADO!')
