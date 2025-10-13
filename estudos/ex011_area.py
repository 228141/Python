#011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

#Eu desenvolvi esse script abaixo e que funcionou:
#largura = int(input('Largura da parede: '))
#altura = int(input('Altura da parede: '))
#área = largura * altura
#tinta = área / 2
#print('A área desta parede é {} metros quadrados. \n Sendo necessário {} litros de tinta para pintar a parede.'.format(área, tinta))

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão de {} x {} e a sua área é de {} m².'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))