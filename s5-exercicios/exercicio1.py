"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""

cont = 0
for num in range(0, 101):

    if num % 3 == 0:
        cont = cont + 1
        print(num)

    if cont >= 5:
        break
