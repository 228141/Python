# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. a multa vai custar R$ 7,00 por cada km acima do limite.

# Solicita a velocidade do carro ao usuário
velocidade = float(input("Digite a velocidade do carro (em km/h): "))

# Verifica se a velocidade ultrapassa o limite
limite = 80
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[4;31m',
         'pretoebranco':'\033[7;30m'}
if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7.00
    print(f"Você foi {cores['vermelho']}MULTADO{cores['limpa']}! Sua velocidade foi {cores['vermelho']}{velocidade} km/h.{cores['limpa']}")
    print(f"O valor da multa é {cores['vermelho']}R$ {multa:.2f}{cores['limpa']}.")
else:
    print("Velocidade dentro do limite. Tenha um bom dia!")

