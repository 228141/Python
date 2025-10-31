# Melhore o jogo do DESAFIO 028, onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogodor vai  tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint # faz o computador 'pensar', ou melhor randomizar números
from time import sleep
computador = randint(0, 10) # Faz o computador "PENSAR"
print('-=-' *20)
print('Sou o computador e vou pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar?...')
print('-=-' *20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? ')) # Jogador tenta adivinhar
    print('PROCESSANDO...')
    sleep(.5)
    palpites += 1
    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Nossa! Você acertou na MOSCA! PARABÉNS!!!')
print('O número que escolhi foi {}, igual ao número que você escolheu {}'.format(computador, jogador))
