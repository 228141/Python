# Crie um programa que leia uma frase qualquer e diga se ela é um "palindromo" desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()

# Com esses dois comandos é possível separar as palavras e depois junta-las para que após possa ser percorrida.
palavras = frase.split() # separa a frase em palavras
junto = ''.join(palavras) # juntas as palavras

# Agora é possivel seguir essa string para ler de trás para frente.
inverso = '' # o inverso vai estar vasio no ínicio

# começa em "len" de junto e ver percorrendo de trás para frente, e pega o númeor de letras digitado na string e vem percorrendo
for letra in range(len(junto) -1, -1, -1): 
#    print(junto[letra], end='')
    inverso += junto[letra]
print('A frase digitada {}, e o seu inverso é {}'.format(junto, inverso, '\033[m'))
if inverso == junto:
    print('\033[32m', 'Isso É um PALÍNDROMO!')
else:
    print('\033[31m', 'Isso NÃO é um PALÍNDROMO', '\033[m')

#print('Você digitou a frase é: {}'.format(junto))