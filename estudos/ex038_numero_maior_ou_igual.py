# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é MAIOR
# O segundo valor é MAIOR
# Não existe valor maios, os dois são IGUAIS

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro número é MAIOR!')
elif num2 > num1:
    print('O segundo numero é MAIOR!')
#elif num2 == num1:
#    print('O segundo numero é MAIOR!')
else:
    print('Os números são IGUAIS!')
