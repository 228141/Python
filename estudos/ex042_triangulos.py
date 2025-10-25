# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado;

#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

print('-=-' * 15)
print('ANALISANDO TRIÂNGULO')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('Tipo EQUILÁTERO!') # todos os lados iguais
    elif r1 != r2 != r3 != r1:
        print('Tipo ESCALENO!') # todos os lados diferentes
    else:
        print('Tipo ISÓCELES!') # um lado igual
else:
    print('Os segmentos acima NÃO PODEM um triângulo!')