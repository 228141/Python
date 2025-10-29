# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizandoo laço for.

num = int(input('Digite um número: '))
print('A tabuada do número escolhido é: ')
print('-=-'*5)
for c in range(1,11):
    print('{} X {:2} = {}'.format(num, c, num*c))
print('-=-'*5)
