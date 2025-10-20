#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} que você digitou é um ano BISSEXTO.'.format(ano))
else: 
    print('O ano {} NÃO é um ano BISSEXTO.'.format(ano))


#OBSERVAÇÃO: Um ano bissexto tem 366 dias, com um dia extra em 29 de fevereiro, para ajustar o calendário ao tempo real que a Terra leva para dar uma volta ao Sol (cerca de 365 dias e 6 horas). Essa correção é importante para que as estações do ano não se desloquem do seu mês correspondente no calendário. Para saber se um ano é bissexto, ele deve ser divisível por 4, com a ressalva de que os anos centenários (como 1900) só são bissextos se forem divisíveis por 400 (como o ano 2000). Neste caso é utilizado: if ano % 4 == 0 and % 100 != 0 or ano % 400 == 0:
