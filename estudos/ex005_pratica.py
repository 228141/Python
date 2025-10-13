5+3*2
5**2
5**3
19//2
19/2
365**522
18%2
122%3
4**3
pow(4,3)
81**(1/2)
25**(1/2)
127**(1/3)
# A junção entre dois
print('Oi'+'Olá')
print('oi' + ' olá')
print('Oi'*5)
print('='*20)

# Recebe a variável normalmente!
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

# A variável recebe 20 caracteres {:20}
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #Dentro da chave tem os ":" dois pontos que significa "DEPOIS", que quer dizer neste caso - depois do valor digitado insira 20 espaços de caracteres

# A variável recebe 20 caracteres com  alinhamento a direita {:>20} 
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))

# A variável recebe 20 caracteres com  alinhamento a esquerda {:<20}
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))

# A variável recebe 20 caracteres com  alinhamento no centro {:^20}
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))

# A variável recebe 20 caracteres com  alinhamento no centro com sinal em volta {:=^20}
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a multiplicação é {}, \n e a divisão é {:.3f}'.format(s,m,d), end = ' &&& ')#esse "end" no final não deixará quebrar a linha, ou mostrará o que foi colocado nele por exemplo &&&. E o "\n" quebra a linha onde foi colocado.
print('A divisão inteira {} e a potência {}'.format(di, e))
