# Manupulando cadeias de caracteres (textos)

🧠 1. Conceito básico

Em Python, string é um conjunto de caracteres (letras, números, símbolos).
Exemplo:

frase = "Python é incrível!"

✂️ 2. Fatiamento (slice)

Permite pegar partes (substrings) da string original.

frase = "Python é incrível!"
print(frase[0])      # P → primeiro caractere
print(frase[0:6])    # Python → do índice 0 até 5
print(frase[7:])     # é incrível! → do índice 7 até o final
print(frase[:6])     # Python → do início até o 5
print(frase[::2])    # Pto  ncrvl → de 2 em 2 caracteres


🧩 Índices negativos contam de trás pra frente:

print(frase[-1])   # ! → último caractere
print(frase[-9:])  # incrível! → últimos 9 caracteres

🔍 3. Análise (verificação e contagem)

Verifica tamanho, busca palavras, conta letras, etc.

frase = "Python é incrível!"
print(len(frase))             # 17 → comprimento
print(frase.count("n"))       # 2 → quantas vezes 'n' aparece
print(frase.find("é"))        # 7 → posição onde aparece
print("Python" in frase)      # True → existe a palavra?
print("Java" not in frase)    # True → não existe?

🔄 4. Transformação

Permite alterar o texto (maiúsculas, minúsculas, trocar palavras, etc.)

frase = "  Python é Incrível!  "
print(frase.upper())     # PYTHON É INCRÍVEL!
print(frase.lower())     # python é incrível!
print(frase.capitalize())# Python é incrível!
print(frase.title())     # Python É Incrível!
print(frase.strip())     # remove espaços extras
print(frase.replace("Python", "Java"))  # troca palavras


Existem também:

frase.lstrip()  # remove espaços à esquerda
frase.rstrip()  # remove espaços à direita

🪓 5. Divisão e Junção

Permite quebrar e unir partes de texto.

➤ split() → divide a string
frase = "Python é incrível"
palavras = frase.split()
print(palavras)  # ['Python', 'é', 'incrível']

➤ '_' .join() → junta as partes
frase_nova = '_'.join(palavras)
print(frase_nova)  # Python_é_incrível


🔹 .split() cria uma lista de palavras
🔹 .join() junta uma lista de strings em uma única string.

🧩 6. Testes com métodos booleanos

Verificam o tipo de conteúdo da string.

print("123".isnumeric())   # True → só números
print("abc".isalpha())     # True → só letras
print("abc123".isalnum())  # True → letras e números
print("python".islower())  # True → tudo minúsculo
print("PYTHON".isupper())  # True → tudo maiúsculo
print("Python".istitle())  # True → cada palavra inicia em maiúscula

🎨 7. Formatação de strings

Existem várias formas de inserir variáveis em strings:

nome = "Jailton"
idade = 40
print("Olá, {}! Você tem {} anos.".format(nome, idade))  # forma clássica
print(f"Olá, {nome}! Você tem {idade} anos.")            # f-string (moderna e recomendada)


💡 Também é possível formatar números:

preco = 5.789
print(f"Preço: R${preco:.2f}")  # duas casas decimais → R$5.79

🧮 8. Outros métodos úteis
Método	Função	Exemplo
startswith("txt")	Verifica se começa com	"Python".startswith("Py") → True
endswith("txt")	Verifica se termina com	"Python".endswith("on") → True
index("txt")	Retorna a posição (erro se não encontrar)	"Python".index("th") → 2
center(20, "-")	Centraliza com preenchimento	"Python".center(20, "-")
zfill(5)	Preenche com zeros à esquerda	"42".zfill(5) → 00042
📚 9. Resumo mental
Categoria	Métodos principais
Fatiamento	[:] [::]
Análise	len(), count(), find(), in
Transformação	upper(), lower(), strip(), replace()
Divisão e Junção	split(), join()
Testes	isalpha(), isnumeric(), isalnum(), islower()
Formatação	format(), f-string
