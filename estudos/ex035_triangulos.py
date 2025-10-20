# Desenvolva um programa que eia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

'''
A regra do triângulo, ou condição de existência de um triângulo, afirma que:
A soma de quaisquer dois lados deve ser maior que o terceiro lado. Por exemplo, para lados de medidas 3, 4 e 5, temos que 3 + 4 > 5, 3 + 5 > 4 e 4 + 5 > 3. 
Um triângulo não pode ser formado se a soma dos dois lados menores for menor ou igual ao lado maior. 
Essa condição é conhecida como desigualdade triangular, que garante que os lados se conectem formando uma figura fechada. 
Essas regras são essenciais para determinar se três segmentos de reta podem formar um triângulo.
'''

print('-=-' * 15)
print('ANALISANDO TRIÂNGULO')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM um triângulo!')