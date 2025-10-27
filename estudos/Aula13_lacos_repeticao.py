# LAÇOS DE REPETIÇÃO

'''
Em português                => forma utilizada no Python
laço c no intervalo(0,3)    =>   for c in range(0,3)
    passo                   =>       passo     
    pula                    =>       pula
passo                       =>   passo
pega                        =>   pega   

'''

# Exemplo
for c in range(1, 6):
    print('Oi')
print('Fim')

# Trocar o "Oi" por "C", é iniciado uma contagem
for c in range(1,6):
    print(c)
print('Fim')

# Contando de 2 em 2, ou a quantidade que quiser:
for c in range (0, 7, 2):
   print(c)
print('Fim')

# Contagem Negativa
for c in range(6, 0, -1):
    print(c)
print('Fim')

#Exemplo de contagem pedindo um número
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('Fim')

# A cada passos de números pulados
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

#Exemplo de repetição dentro do laço, com comando de input
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

# Somando os valores 
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores é {}'.format(s))

