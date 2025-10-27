# Crie um programa que mostre na tela "todos os números pares" que estão no intervalo entre 1 e 50.

#contagem normal
#for cont in range(1,51): 
    #print(cont)
#    print(cont, end=' ') # o "end=' ' ", serviu para colocar na mesma linha a contagem.

# Primeira forma de fazer o exercício:
#for cont in range(1, 51):
#    print('.', end=' ') # com esse ponto, consigo saber quantas vezes o laço de repetição realizou interação, dessa forma consigo até melhorar o código
#    if cont % 2 == 0:
#        print(cont, end=' ')
#print('-=-Todos os números pares entre 1 e 50.-=-')

# Melhorando o código acima:
#for cont in range(2, 51):
#    print('.', end=' ') # com esse ponto, agora conseguimos ver o laço se repetiu uma vez
#    print(cont, end=' ')
#print('-=-Todos os números pares entre 1 e 50.-=-')

#Desta forma conseguimos ter um código mais enxuto e que ocupa menos espaço no computador
for cont in range(2, 51, 2):
    print(cont, end=' ')
print('-=-Todos os números pares entre 1 e 50.-=-')

