# AULA 10 - CONDIÇÕES SIMPLES E COMPOSTA

'''EXEMPLO
carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão 
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()
'''

#Blocos
'''
se carro.esquerda()
    bloco_V_
senão
    bloco_F_
'''
# Condição (Estrutura Condicional)
'''
if carro.esquerda():
    bloco True
else:
    bloco False
'''
#Exemplo
'''
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print("Carro Velho")
print('--FIM--')
'''

#Simplificando
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro Novo' if tempo <= 3 else "Carro Velho")
print('--FIM--')
