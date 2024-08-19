"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele 
possui.

"""

numbers = []

for i in range(0,10):
    numbers.append(int(input(f"Digite o numero da posição {i+1}: ")))

pares = 0
for valor in numbers:
    if(valor % 2 == 0):
        pares = pares + 1

print(f"A lista possui {pares} pares")