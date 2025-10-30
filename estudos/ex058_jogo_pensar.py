# Melhore o jogo do DESAFIO 028, onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogodor vai  tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Nossa! Você acertou na MOSCA! PARABÉNS!!!')
    print('O número que escolhi foi {}, igual ao número que você escolheu {}'.format(computador, jogador))
else:
    print('Que pena, você errou')
    print('O número que escolhi foi {}, e não o número {}'.format(computador, jogador))
