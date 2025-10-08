# DESAFIO - Faça um programa que leia algo pelo teclado e mostre na telao seu tipo prmitivo e todas as informaçõesa possíveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo digitado é: ',type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
