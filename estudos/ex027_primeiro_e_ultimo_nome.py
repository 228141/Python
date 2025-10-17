# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Útimo: Souza

n = str(input("Digite seu nome: ")).strip()
nome = n.split()
print('Muito Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

# OBSERVAÇÃO: "split" irá pegar o nome inteiro e irá fatiar ou dividir em pedaços 
