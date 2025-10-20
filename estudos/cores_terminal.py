#Cores no terminal no PYTHON
'''
Código ANSI - escape sequence
\033[STYLE, TEXT, BACK m

EXEMPLO:
\033[0:33:44m

STYLE
0 - NONE
1 - BOLD
4 - UNDERLINE
7 - NEGATIVE

TEXT
30 - BRANCO
31 - VERMELHO
32 - VERDE
33 - AMARELO
34 - AZUL
35 - VIOLETA
36 - AZUL CLARO
37 - CINZA

BACK (FUNDO)
40 - BRANCO
41 - VERMELHO
42 - VERDE
43 - AMARELO
44 - AZUL
45 - VIOLETA
46 - AZUL CLARO
47 - CINZA

print('\033[4:30:41mOlá Mundo!!! \033[m')

nome = 'Jailton Pereira'
print('Olá muito prazer em te conhecer, {}{}{}!!!'.format('\033[4.34m', nome, '\033[m'))'''

#Exemplo usando dicionário
nome = 'Jailton Pereira'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[4;31;46m',
         'pretoebranco':'\033[7;30m'}
print('Olá muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, '\033[m'))


