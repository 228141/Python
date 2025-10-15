# Grupos de bibliotecas
# comandos pode ser dados para importar as bibliotecas ("import doces", importa todas as funcionalidades sendo mais generalista)
# E pode ser importados apenas o que é preciso ("from doce import pudim", importa apenas o que precisa sendo mais restrita)
# biblioteca matemática "math" = (com o comando "import math", será importado toda a biblioteca)
# biblioteca "math" = (com o comando "from math import sqrt, ceil", será importado apenas a funcionalidade squer ruth e ceil)
# ceil = arredonda o número para cima
# floor = arredonda o número para baixo
# trunc
# pow
# sqrt = raiz quadrada
# factorial

#Exemplo

import math
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) #mostra o valor sem arredondamento

import math
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # arredonda o resultado para cima

import math
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) #arrendonda o resultado para baixo

#importanto apenas uma funcionalidade
from math import sqrt, floor
num = int(input('Digite um número'))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) 
