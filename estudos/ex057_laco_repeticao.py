# Faça um programa que leia o "sexo" de uma pessoa, mas só aceite os valores "M" OU "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #strip tira os espaços antes e depois de digitado e o upper é transformado para maiusculas, sendo após com o 'zero' para pegar a primeira letra digitada
while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor informe o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))