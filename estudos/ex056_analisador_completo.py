# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo
# Quantas mulheres têm menos de 20 anos
# Qual é o nome do homem mais velho

# Inicializando variáveis
soma_idades = 0
mulheres_menos_20 = 0
homem_mais_velho_nome = ''
homem_mais_velho_idade = 0

# Loop para ler dados de 4 pessoas
for i in range(1, 5):
    print('------ {}ª Pessoa ------'.format(i))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    soma_idades += idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    if sexo == 'M':
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome

# Resultados
media_idade = soma_idades / 4
print("\n--- Resultados ---")
print(f"Média de idade do grupo: {media_idade:.1f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
print(f"A idade do homem mais velho tem {homem_mais_velho_idade} anos e se chama: {homem_mais_velho_nome}")
