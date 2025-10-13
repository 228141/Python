#008 - Escreva um programa que leia um valor em metros e exiba o valor convertido em centimetros e milimetros.

metro = float(input('Uma distância em metros: '))
print('O media de {} metros corresponde à \n {:.0f} centimetros \n {:.0f} milimetros'.format(metro, metro * 100, metro * 1000))

#Desafio: Faça também todas os Múltiplos do metro: 
# decímetro (dm) = 0,1 metro (m).
# centímetro (cm) = 0,01 metro (m). 
# milímetro (mm) = 0,001 metro (m).
# Metro (m)
# quilômetro (km) = 1000 metros (m).
# hectômetro (hm) = 100 metros (m).
# decâmetro (dam) = 10 metros (m). 

metro = float(input('Uma distância em metros: '))
print('O conversão de {} metros corresponde \n {:.0f} decímetro, \n {:.0f} centimetros, \n {:.0f} milimetros, \n {} quilômetros, \n {} hectômetros, \n {} decâmetros'.format(metro, metro*10, metro * 100, metro * 1000, metro / 1000, metro / 100, metro / 10))