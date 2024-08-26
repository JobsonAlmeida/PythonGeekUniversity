"""
Trabalhando com módulos built-in (módulos integrados que já vem instalados no Python)

__________________________
|Python|Módulos built-in|
__________________________

"""

# Utilizando alias (apelidos) para módulos ou funções

import random as rdm # Fazendo esse tipo de importação, para utilizar as funções é necessário
                     # utilizar o nome do escopo

print(rdm.random())

from random import randint as rdi

print(rdi(5,89))

#importando duas funções

from random import randint as rdi, random as rdm

print(rdi(5,89))
print(rdm())

# Podemos utilizar todas as funções de um módulo utilizando o *

from random import * # Fazendo esse tipo de importação, para utilizar as funções não é necessário
                     # utilizar o nome do escopo. Basta apenas utilizar o nome da função.
                     # Atenção que aqui está sendo importado todas as funções

print(random())

# importando todo o módulo

import random
print(random.random())

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3,7))
lista = [2,3,4,5,6]
shuffle(lista)
print(lista)
print(choice("university"))

