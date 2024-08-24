"""
Zip

zip -> cria um iteravel chamado zip object que agraga elementos de cada um dos iteráveis passado como entrada
em pares

a partir do iterável retornado podemos gerar uma lista, tupla, conjunto ou um dicionário


"""


lista1 = [1,2,3]
lista2 = [4,5,6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

zip1 = zip(lista1, lista2)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# Obs.: O zip utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estivermos trabalhando
# com iteráveis de tamanho diferentes, irá parar quando os elementos do menos iterável acabar
lista1 = [1,2]
lista2 = [4,5,6]
lista3 = [7,8,9,10,11,12] 

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com a função zip

tupla = 1,2,3,4,5
lista = [6,7,8,9,10]
dicionario = {'a':11, 'b':12, 'c':13, 'd':14, 'e':15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]

"""
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]

zip(*dados)

Doing this, it's similar as we are passing five tuples with two elements each one to the function zip

zip( (0,1), (1,2), (2,3), (3,4), (4,5) ) 

Therefore, we create a iterabla like

(0,1)
(1,2)
(2,3)
(3,4)
(4,5)
(0,1,2,3,4,5), (1,2,3,4,5) -> resulting iterable formed by tuples. And we can convert this iterable as 
a list, tuple, set or even as a dictionary  

"""
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*dados)))

# Exemplos mais complexos


prova1= [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ["maria", "pedro", "carla"]

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2) ))
print(dict(final))