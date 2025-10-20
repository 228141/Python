# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar. 

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('O número {} digitado é PAR.'.format(num))
else:
    print('O número {} digitado é IMPAR'.format(num))

# (Ex: 5 // 2 == 2) - divisão inteira é o resultado da divisão em que consta o resto da divisão, e o resultado é apenas o número dessa divisão, 5/2 é igual a 2 resta 1, então o valos da conta é 2
# (Ex: 5 % 2 == 1) - porcentagem deste valor é o resto da divisão inteira.