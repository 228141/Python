# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entres eles(desconsiderando o flag).

print('-'*35)
print('Sequencia de Números')
print('-'*35)
num = cont = soma = 0
num = int(input('Digite um número [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar] '))
print('Você digitou {} números e a soma  entre foi {}.'.format(cont, soma))