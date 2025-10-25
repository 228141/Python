# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcula seu IMC e mostre seu staus, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideial
# Entre 25 até 30: Sobrepeso
# Entre 30 até 40: Obesidade
# Acima 40: Mórbida

peso = float(input('Qual o seu peso(Kg)? '))
altura = float(input('Qual a sua altura(m)? '))
imc = peso / (altura ** 2) 
print('O IMC desta pessoa é: {:.1f}!'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está no Peso Ideal!')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em Obsesidade!')
elif imc >= 40 :
    print('Você esta em Obesidade Mórbida, cuidado!')

'''
IMC = peso (kg) / altura² (m).
Por exemplo, se você pesa 70 kg e tem 1,70 m de altura, o cálculo seria: 70 / (1,70 x 1,70) = 24,22'''