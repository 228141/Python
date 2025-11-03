# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print('=' * 36)
print('GERADOR DE PA - MELHORANDO O CÓDIGO')
print('=' * 36)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{}, '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais '))
print('FIM')
