#Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para a viagem de até 200 km, e R$ 0,45 para viagens mais longas.

distância = float(input('Qual a distância da viagem? '))
print('Você está prestes a comecar uma viagem de {:.1f}km'.format(distância))
if distância <= 200: 
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))

# Modo simplificado

distância = float(input('Qual a distância da viagem? '))
print('Você está prestes a comecar uma viagem de {:.1f}km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))





