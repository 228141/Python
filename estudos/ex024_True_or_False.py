# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "Santo"

#strip funciona para eliminar os espaços na frente e após

cid = str(input('Em que cidade você nasceu? ')).strip() 
print(cid[:5].upper() == 'SANTO')