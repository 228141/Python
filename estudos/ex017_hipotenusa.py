# Faça um programa que leia o comprimento que leia o cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

''' Modo comum de realizar o calculo sem a biblioteca
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
