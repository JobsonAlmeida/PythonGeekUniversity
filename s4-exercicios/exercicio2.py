"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.

"""
import math

num = int(input("The the number you want: "))

if num >= 0:
    print(f"The square root of {num} is", math.sqrt(num))
else:
    print(f"The number {num} is invalid.")

