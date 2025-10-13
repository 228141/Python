#007 - Desenvolva um progrmama que leia as duas notas de um aluno, calcule e mostre a sua média.
#Dica: conferir o resultado e ver se o valor está certo, neste caso pode ser ordem de precedencia.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
média = (nota1 + nota2) / 2
print('A nota média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, média))

#Outra forma de visualizar o exercicio
#nota1 = float(input('Primeira nota do aluno: '))
#nota2 = float(input('Segunda nota do aluno: '))
#soma = nota1 + nota2
#print('A sua nota média é {}'.format(soma / 2))