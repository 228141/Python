# Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('-=-A soma de todos os {}, divisíveis por 3, de todos valores solicitado é {}.-=-'.format(cont, soma))