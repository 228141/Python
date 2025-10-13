#009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# eu desenvolvi esse mostro abaixo que funcionou, porém tem outra forma de fazer mais fácil.
#n = int(input('Digite um número: '))
#print('A tabuada deste número é igual a: \n {} X 1 = {} \n {} X 2 = {} \n {} X 3 = {} \n {} X 4 = {} \n {} X 5 = {} \n {} X 6 = {} \n {} X 7 = {} \n {} X 8 = {} \n {} X 9 = {} \n {} X 10 = {}'.format(n, n * 1, n, n * 2, n, n * 3, n, n * 4, n, n * 5, n, n * 6, n, n * 7, n, n * 8, n, n * 9, n, n * 10))

num = int(input('Digite um número: '))
print('-'*13)
print('{} X {:2} = {}'.format(num, 1, num*1))
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}'.format(num, 10, num*10))
print('-'*13)