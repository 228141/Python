# Operações Aritiméticas

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão

# Quando aparecer um simbolo de igual (=) é um sinal de atríbuição, quer dizer que "recebe" algo 
# Já quando aparecer dois simbolos de iguais(==), quero testar se algo mais outro é igual ao resultado:
# (Ex: 5 + 2 == 7)
# (Ex: 5 - 2 == 3)
# (Ex: 5 * 2 == 10)
# (Ex: 5 / 2 == 2.5)
# (Ex: 5 ** 2 == 25)
# (Ex: 5 // 2 == 2) - divisão inteira é o resultado da divisão em que consta o resto da divisão, e o resultado é apenas o número dessa divisão, 5/2 é igual a 2 resta 1, então o valos da conta é 2
# (Ex: 5 % 2 == 1) - porcentagem deste valor é o resto da divisão inteira.

# ORDEM DE PRECEDÊNCIA
# A ordem para resolução é:
# 1º - Parenteses ()
# 2º - Exponenciação **
# 3º - Mutiplicação, divisão, divisão inteira e resto da divisão-OBS: Faz quem aparecer primeiro (*,/, //, %)
# 4º - Adição ou Subtração (+ ou -)

# Exemplos:
# 5 + 3 * 2 == 11 (Resultado: Primeiro faz a multiplicação e depois a soma)
# 3 * 5 + 4 ** 2 == 31 (Resultado: Primeiro faz a potenciação 4**2==16, depois faz a multiplicação 3*5==15 e no final a soma o resultado da potenciação com o resultado multiplicação 16+15==31)

# No caso de existir parenteses na conta, significa que há precedencia para realizar o que está dentro do parenteses primeiro. 
# 3 * (5 + 4) ** 2 == 243 (Resultado: Primeiro faz a soma dentro do parenteses (5 + 4 == 9), depois faz a potenciação (Nove elevado ao quadrado ou 9 vezes 9 == 81) e no final a multiplicação ( 81 vezes 3 == 243)
