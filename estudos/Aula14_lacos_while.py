# Os laços while são uma das estruturas fundamentais em Python para repetir ações enquanto uma condição for verdadeira.
# Vamos entender de forma simples, prática e com exemplos 👇

# 🔷 O que é o while?

# O comando while significa literalmente "enquanto".
# Ele repete um bloco de código enquanto uma condição lógica for verdadeira (True).

# 🧠 Estrutura básica
# while condição:
    # bloco de código
    # (será repetido enquanto a condição for verdadeira)


# ➡️ Quando a condição se torna falsa, o laço para.
'''
🎯 Exemplo simples
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

🔍 O que acontece:

Começa com contador = 1

Verifica contador <= 5

Imprime e soma 1 a cada repetição

Quando contador vira 6, a condição é falsa e o laço termina.

🟢 Saída:

1
2
3
4
5

⚠️ Cuidado: Laço infinito

Se você esquecer de atualizar a variável dentro do while, ele nunca termina:

x = 1
while x <= 5:
    print(x)
# ⚠️ ERRO: nunca aumenta o valor de x → laço infinito


Sempre verifique se algo muda dentro do laço para que a condição um dia se torne falsa.

🔄 Comandos de controle úteis
🔹 break

Interrompe o laço antes da condição ficar falsa.

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    print(f"Olá, {nome}!")


🟢 Para o laço quando o usuário digita “sair”.

🔹 continue

Pula o restante do bloco e volta para o início do laço.

n = 0
while n < 5:
    n += 1
    if n == 3:
        continue  # pula o número 3
    print(n)


🟢 Saída:

1
2
4
5

🔢 Exemplo prático: soma de números até o usuário digitar 0
soma = 0
n = int(input("Digite um número (0 para sair): "))

while n != 0:
    soma += n
    n = int(input("Digite outro número (0 para sair): "))

print(f"A soma total é {soma}")


🟢 O programa só para quando o usuário digita 0.

'''

'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim') '''

'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares.".format(par, impar))
