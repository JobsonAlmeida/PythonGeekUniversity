"""
Map 

Com map, fazemos mapeamento de valores para função



"""

import math

def area(r):
    """Calcula a área de um círculo com raio 'r' """
    return math.pi * (r**2)

print(area(2))
print(area(5.3))

raios = [2,3,5,7.1,8.3, 10, 44]


# Forma comum
areas = []

for r in raios:
    areas.append(area(r))

print(areas)


# Forma com map
# Map é uma função que recebe dois parâmetros. O primeiro parâmetro é a função, o segundo um iterável. Retorna
# um map object. Esse objeto map object pode ser convertido para lista, tupla, para set ou para dicionario.  
# O map mapeia os dados do iterável para a função. Ele pega cada um dos dados do iterável e aplica como
# entrada para a função

print("----areas----")
areas = map(area, raios)
print(areas)
print(type(areas))
print(tuple(areas))

print("---------")

# Map com lambda

print(list(map(lambda r: math.pi*(r**2), raios)))


print("-------------------")

# Após utilizar o objeto map retornado pela função map, esse objeto é zerado. Isso é interessante
# para limpar a memória 

map1 = map(lambda r: math.pi*(r**2), raios)
print(list(map1))
print(list(map1))
print(list(map1))
print(map1)

# Para fixar - Map

# Temos dados iteráveis

# dados : a1, a2, ... , an

# temos uma função f(x)

# Utilizamos a função map(f, dados ) onde map irá 'mapear' cada elemento dos dados e aplicar a função
# O map Object f(a1), f(a2), ... f(an)

# Mais um exemplo

cidades  = [("Berlim", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokio", 27), ("Nova York", 28)]

print(cidades)

c_para_f = lambda dado: ( dado[0], (9/5)*dado[1] + 32) 

cidades_f = map(c_para_f, cidades)
print(list(cidades_f))
