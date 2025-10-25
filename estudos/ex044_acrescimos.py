# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:

# À vista dinheiro / cheque: 10 % de desconto
# À vista cartão 5 % de desconto
# Em 2 vezes no cartão preço normal
# Em 3 vezes ou mais no cartão - 20 % de juros

print('{:=^35}'.format(' LOJAS DA MODA '))
preço = float(input('Qual o preço das compras: R$ '))
print('-=-' * 15)
print('''FORMA DE PAGAMENTO: 
[ 1 ] - À vista dinheiro / cheque
[ 2 ] - À vista cartão
[ 3 ] - 2 X no cartão
[ 4 ] - 3 x ou mais no cartão''')
print('-=-' * 15)
opção = int(input('Escolha sua opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço *5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2X de R$ {:.2f}, SEM JUROS!'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparcel = int(input('Quantas Parcelas? '))
    parcela = total / totparcel
    print('Sua compra parcelada em {}X de R$ {:.2f}, COM JUROS!'.format(totparcel,parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))
