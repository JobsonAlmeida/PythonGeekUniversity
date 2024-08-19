"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores 
lidos.
"""

numbers = [] 
for i in range(0,6):
    number = int( input(f"Digite o número {i+1}: ") )
    numbers.append(number)

print("Os números digitados foram:")
for i in range(0,6):
    print(numbers[i], end = " ") 