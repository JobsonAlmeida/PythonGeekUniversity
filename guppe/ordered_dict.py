"""
Módulo collections - Ordered Dict



"""

#Em um dicionário a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')


# OrderedDict -> é um dicionário que nos garante a ordem de inserção dos elementos
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# 

dict1 = {'a':1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print("dict1")
for chave, valor in dict1.items():
    print(f'chave={chave}: valor={valor}')

print("dict1")
for chave, valor in dict2.items():
    print(f'chave={chave}: valor={valor}')

print(dict1 == dict2) # True já que a ordem dos elementos não importa para o dicionario

odict1 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
odict2 = OrderedDict({'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 1, })

print(odict1 == odict2)