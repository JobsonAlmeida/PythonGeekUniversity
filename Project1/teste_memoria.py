"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

"""

# função usando listas 449MB
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b # the variables at left takes the old values from the variables at right
                      # a=1, b=2, / a=2 b = 3/ a=3 b=
    return  nums

# for n in fib_lista(10000):
#     print(n)

# função usando geradores

def fib_gen(max):

    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a+b
        yield a
        contador = contador + 1


for n in fib_gen(100000):
    print(str(n))

