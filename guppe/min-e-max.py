"""
Min e Maxx

max -> retorna o maior valor em um iteravel, ou o maior de dois ou mais elementos

min -> retorna o menor valor em um iteravel, ou o menor de dois ou mais elementos

"""

# lista = [1,3,5,8,9,12,56, 234, 4,2]
# print(max(lista))

# tupla = (1,3,5,8,9,12,56, 234, 4,2)
# print(max(tupla))

# set = {1,3,5,8,9,12,56, 234, 4,2}
# print(max(set))

# dicionario = {'a':1,'b': 3, 'c': 5,'d': 8,'e': 9,'f': 12,'g': 56,'h': 234, 'i': 4,'k':2}
# print(max(dicionario.values()))

# print(max(3,34))

# val1= int(input("Informe o primeiro valor: "))
# val2= int(input("Informe o segundo valor: "))

# print(max(val1, val2))


# print("------")

# lista = [1,3,5,8,9,12,56, 234, 4,2]
# print(min(lista))

# tupla = (1,3,5,8,9,12,56, 234, 4,2)
# print(min(tupla))

# set = {1,3,5,8,9,12,56, 234, 4,2}
# print(min(set))

# dicionario = {'a':1,'b': 3, 'c': 5,'d': 8,'e': 9,'f': 12,'g': 56,'h': 234, 'i': 4,'k':2}
# print(min(dicionario.values()))

# val1= int(input("Informe o primeiro valor: "))
# val2= int(input("Informe o segundo valor: "))
# print(min(val1, val2))


# Outros exemplos
print("--- outros exemplos ----")

nomes = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32},
    {"titulo": "Joao Avelino", "tocou": 32},
    {"titulo": "Carla", "tocou": 32},

]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

# Desafio

musica_max = max(musicas, key=lambda musica: musica["tocou"])
musica_min = min(musicas, key=lambda musica: musica["tocou"])

print(f"Título da mais tocada: {musica_max["titulo"]}")
print(f"Título da menos tocada: {musica_min["titulo"]}")

# 