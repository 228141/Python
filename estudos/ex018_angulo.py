# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, do cosseno e a tangente desse ângulo

#Importando toda a biblioteca
'''
import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, coseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
'''
#Importando apenas os metodos utilizados
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, coseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))