"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

num = int(input("Type the number you want: "))

if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f'The number {num} is odd')
