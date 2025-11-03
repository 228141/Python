#Faça um programa que leia um número qualquer e mostre o seu fatorial. EX: 5! = 5X4X3X2X1 = 120
'''
#from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
#f = factorial(n)
c = n
f = 1 #para calcular o fator do número, deve se começar com 1, pois se começar com zero o resultado irá zerar a conta  
print('Calculando {}!'.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print('{}'.format(f))
#print('O fatorial de {} é {}.'.format(n, f))
'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
c = n
print('O fatorial de {} é {}.'.format(n, f))

