"""
Módulo Collections - Named Tuple

Named Tuple -> são tuplas onde especificamos um nome para a mesma e também parâmetros

"""


tupla = (1, 2, 3)
print(tupla[1])

from collections import namedtuple

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro = namedtuple("cachorro", 'idade, raca, nome')

# Forma 3

cachorro =namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca="chow-chow", nome="Ray")
print(ray)


#Acessando os dados

#Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)


print(ray.index("chow-chow"))
