#012 - Faça um algoritimo que leia o preço de produto e mostre o novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
novo_preco = preco - (preco * 5 / 100)
print('O produto custava R$ {:.2f}, na promoção com desconto de 5%, vai custar R${:.2f}'.format(preco, novo_preco))
