"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

print("--Type two numbers--")

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))

if num1 > num2:
    print(f'Number {num1} is the greatest.')
elif num1 == num2:
    print(f'The two numbers typed are equal.')
else:
    print(f'Number {num2} is the greatest.')
