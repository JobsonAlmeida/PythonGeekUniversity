"""
Reduce

Obs: A função reduce já foi uma função integrada (built-in)
 A partir do Python3+ a função reduce não é mais uma função integrada built-in. Agora temos que importar e utilizar
 esta função a partir do módulo 'functools'

 Guido Van Rossum (criador da linguagem python): Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um
 loop for é mais legível


Assim como map e filter, a função reduce recebe dois parâmetros: a função e o iterável

reduce(funcao, dados)


vale lembrar que para utilizar a função reduce nós precisamos de uma função que recebe dois parâmetros


"""

# Uilizando reduce para multiplicar todos os numeros de uma lista
from functools import reduce

dados = [2,5,3,4,5,6,34,5,66]

multi = lambda x,y: x*y

res = reduce(multi, dados)

print(res)

# utilizando um loop normal
res = 1
for n in dados:
    res = res *n

print(res)





