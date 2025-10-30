# LAÇOS DE REPETIÇÃO

O que são condições aninhadas?

Condições aninhadas acontecem quando uma estrutura condicional (if) está dentro de outra, permitindo fazer decisões mais detalhadas dependendo de várias situações.

É como fazer perguntas em etapas:

➡️ Se isso for verdade, então verifique aquilo.

🧠 Estrutura básica
if condição1:
    # código se condição1 for verdadeira
    if condição2:
        # código se condição2 também for verdadeira
    else:
        # código se condição2 for falsa
else:
    # código se condição1 for falsa

🎯 Exemplo prático

Vamos verificar a idade de uma pessoa e definir sua fase da vida:

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
    if idade >= 60:
        print("Você é idoso.")
    else:
        print("Você é adulto.")
else:
    print("Você é menor de idade.")

🧩 Interpretação:

Primeiro verifica se é maior de idade.

Dentro desse bloco, verifica se é idoso.

Se não for maior, já sabe que é menor de idade.

✅ Quando usar condições aninhadas?

🔹 Quando o segundo teste depende do resultado do primeiro
🔹 Para evitar verificar condições desnecessárias
🔹 Para organizar decisões complexas em etapas lógicas

🚫 Cuidado para não exagerar

➡️ Muita aninhamento pode deixar o código confuso.
➡️ Sempre que possível, prefira usar elif para múltiplas condições:

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

🎓 Conclusão rápida:
Termo	                  //      O que significa
if dentro de outro if	  =>      Condição aninhada
Útil para	              =>      Verificar situações dependentes
Alternativa melhor	      =>      Usar elif quando as condições são independentes

'''
Em português                => forma utilizada no Python
laço c no intervalo(0,3)    =>   for c in range(0,3)
    passo                   =>       passo     
    pula                    =>       pula
passo                       =>   passo
pega                        =>   pega   

'''

# Exemplo
for c in range(1, 6):
    print('Oi')
print('Fim')

# Trocar o "Oi" por "C", é iniciado uma contagem
for c in range(1,6):
    print(c)
print('Fim')

# Contando de 2 em 2, ou a quantidade que quiser:
for c in range (0, 7, 2):
   print(c)
print('Fim')

# Contagem Negativa
for c in range(6, 0, -1):
    print(c)
print('Fim')

#Exemplo de contagem pedindo um número
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('Fim')

# A cada passos de números pulados
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

#Exemplo de repetição dentro do laço, com comando de input
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

# Somando os valores 
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores é {}'.format(s))

