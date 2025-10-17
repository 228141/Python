#Exemplos de estrutura condicional simples
'''
nome = str(input('Qual o eu nome? ')).strip()
if nome == 'Ana':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

#Exemplos de estrutura condicional simples

nome = str(input('Qual o eu nome? ')).strip()
if nome == 'Ana':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''
'''
#ESTRUTURA CONDICIONAL
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
'''

#Condição Simplificada

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!')
