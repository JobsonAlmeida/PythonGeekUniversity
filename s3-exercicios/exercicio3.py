"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""

number1 = int(input("Type the the first number: "))
number2 = int(input("Type the the second number: "))
number3 = int(input("Type the the third number: "))

sum_square = number1**2 + number2**2 + number3**2

print(f'The sum between the squares of the numbers {number1}, {number2} and {number3} is {sum_square}')