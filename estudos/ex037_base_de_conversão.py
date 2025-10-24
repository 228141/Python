#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a "base de conversão":
# 1- para binário / 2 - para octal / 3 - para hexadecimal 

# Solicita um número inteiro ao usuário
print('BASE DE CONVERSÃO')
numero = int(input("Digite um número inteiro: "))

# Exibe as opções de conversão
print('-=-' * 10)
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
print('-=-' * 10)

# Lê a escolha do usuário
opcao = int(input("Sua opção: "))

# Realiza a conversão com base na escolha
if opcao == 1:
    print(f"{numero} convertido para BINÁRIO é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para OCTAL é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido para HEXADECIMAL é {hex(numero)[2:].upper()}")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

'''
# Outra forma de fazer esse exercício

numero = int(input("Digite um número inteiro: "))
print(***Escolha uma das bases paraa conversão:
[ 1 ] - converter para Binário
[ 2 ] - converter para Octal
[ 3 ] - converter para Hexadeimal***) # No lugar dos asteriscos substituir para tres aspas simples
opcão = int(input("Sua opção: "))
if opcão == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:] ))
elif opcão == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:] ))
elif opcão == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:] ))
else:
    print("Opção inválida. Por favor SOMENTE escolha 1, 2 ou 3.")
'''
