'''
🔷 O que são condições aninhadas?

Condições aninhadas acontecem quando uma estrutura condicional (if) está dentro de outra, permitindo fazer decisões mais detalhadas dependendo de várias situações.

É como fazer perguntas em etapas:

➡️ Se isso for verdade, então verifique aquilo.

if condição1:
    # código se condição1 for verdadeira
    if condição2:
        # código se condição2 também for verdadeira
elif:
        # código se condição2 for falsa
else:
    # código se condição1 for falsa


🎯 Exemplo prático

Vamos verificar a idade de uma pessoa e definir sua fase da vida:

idade = int(input("Digite sua idade: "))
'''

idade = int(input("Digite sua idade: "))

if idade >= 18: 
    print("Você é maior de idade.")
    if idade >= 60:
        print("Você é idoso.")
    else:
        print("Você é adulto.")
else:
    print("Você é menor de idade.")

