# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevedo o nome escolhido.

#Observação: Na Aula 8 foi falado sobre o "random", que é a biblioteca de escolhas do sistema

from random import choice
n1 = str(input("Primeiro Aluno:"))
n2 = str(input("Segundo Aluno:"))
n3 = str(input("Terceiro Aluno:"))
n4 = str(input("Quarto Aluno:"))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)#choice da classe random funciona com a escolha aleatória
print('O aluno sorteado foi {}'.format(sorteado))