# Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('-=-'*10)
print('-=-PROGRAMA DE MENU!-=-')
print('-=-'*10)
num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
opção = 0
while opção != 5:
    print('-=-'*10)
    print('''Escolha sua opção: 
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior número
    [ 4 ] - Novos Números
    [ 5 ] - Sair do Programa''')
    print('-=-'*10)
    opção = int(input('Qual opção você deseja? '))
    if opção == 1:
        soma = num1 + num2
        print('Você escolheu a opção {}.'.format(opção))
        print('A soma entre primeiro número {} e o segundo número {} é igual a {}.'.format(num1, num2, soma))
    elif opção == 2:
        produto = num1 * num2
        print('Você escolheu a opção {}.'.format(opção))
        print('A multiplicação entre primeiro número {} e o segundo número {} é igual a {}.'.format(num1, num2, produto))
    elif opção == 3:
        print('Você escolheu a opção {}.'.format(opção))
        if num1 > num2:
            print('Entre {} e {}, o maior valor é {} e o menor é {}.'.format(num1, num2, num1, num2))
        elif num2 > num1:
            print('Entre {num1} e {num2}, o maior valor é {num2} e o menor é {num1}.'.format(num1, num2, num1, num2))
        else:
            print('Os números são IGUAIS: {} e {}.'.format(num1, num2))
    elif opção == 4:
        print('Informe os números novamente: ')
        print('Você escolheu a opção {}.'.format(opção))
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
    elif opção == 5:
        print('Você escolheu a opção {}.'.format(opção))
        print('Finalizando...')
    else:
        print('Opção Inválida, tente novamente!')
    sleep(2)
print('Fim do programa, volte sempre!')
