#006 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo, e raiz quadrada.

#Guardando a variável
#alg = int(input('Digite um número: '))
#dob = alg * 2 
#trp = alg * 3
#e = alg ** (1/2)
#print('O dobro de {}, vale {}, \n O triplo é {}, \n E a raiz quadrada é {:.2f}'.format(alg ,dob, trp, e))

# Outra forma de realizar o exercício
#alg = int(input("Digite um número: "))
#print('O dobro de {} vale {}'.format(alg, (alg * 2)))
#print('O triplo de {} vale {} \n E a raiz quadrada de {} é igual {:.2f}'.format(alg, (alg * 3), alg, (alg ** 2))) 
# #para elevado ao quadrado também funciona pow(alg, 2)

# Outra forma de realizar o exercício
alg = int(input("Digite um número: "))
print('O dobro de {} vale {} \n O triplo de {} vale {} \n E elevado ao quadrado de {} é igual {:.2f}'.format(alg, alg * 2, alg, alg * 3, alg, pow(alg, 2)))

