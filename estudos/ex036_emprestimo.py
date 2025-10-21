# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela ão pode exceder 30% do salário ou então o empréstimo será negado.

# Solicita os dados do comprador
valor_casa = float(input("Digite o valor da casa (R$): "))
salario = float(input("Digite o salário do comprador (R$): "))
anos = int(input("Em quantos anos pretende pagar? "))

# Calcula a prestação mensal
meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

# Verifica se a prestação excede 30% do salário
print('Comparando: A prestação mensal É de R$ {:.2f} e 30% do seu salário é de R$ {:.2f}'.format(prestacao, limite))
if prestacao > limite:
    print(f"\033[1;31mEmpréstimo NEGADO!\033[m A prestação mensal de R$ {prestacao:.2f} excede 30% do salário.")
else:
    print(f"\033[1;32mEmpréstimo APROVADO!\033[m A prestação mensal será de R$ {prestacao:.2f} por {meses} meses.")
  
