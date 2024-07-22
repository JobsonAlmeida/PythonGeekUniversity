"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""

"""
num: int = 0
while num <= 100_000:
    print(num)
    num += 1000
"""

for n in range(0, 100001, 1000):
    print(n)

