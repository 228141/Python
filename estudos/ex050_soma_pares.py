# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se o númeo digitado for impar, desconsidere.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont +1
print('-=-Você informou {} números e a soma de todos os pares é {}.-=-'.format(cont, soma))
