#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a "base de conversão":
# 1- para binário / 2 - para octal / 3 - para hexadecimal 

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Exibe as opções de conversão
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

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
