# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
c = float(input('Informe a temperatura em °C:'))
f = 9 * c / 5 + 32
print('A temperatura informada é {:.1f}°C corresponde a {:.1f}°F'.format(c, f))
