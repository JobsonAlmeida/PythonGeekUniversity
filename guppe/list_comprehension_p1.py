"""
List Comprehension (Compreensão de Lista)

- Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe

'variavel_lista' = [dado_processado for dado in iteravel ]
Eu quero criar uma lista com varios 'dado_processado' para cada 'dado' presente em 'iteravel'. A lista gerada
atribuída para 'variavel_lista' 

"""

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

res = [numero/2 for numero in numeros]

print(res)

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehension x loop

#usando loop 
numeros  = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero*2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#Usando list comprehension
print([numero*2 for numero in numeros])

# Outros exemplos

# 1

nome = "Geek university"

print([letra.upper() for letra in nome])

# 2

amigos = ['maria', "julia", 'pedro', 'guilherme', 'vanessa']

print([amigo[0].upper()+amigo[1:] for amigo in amigos])
print([amigo.title() for amigo in amigos])

# 3

print([numero*3 for numero in range(1,10)])

# 4 

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1,2,3,4,5]])

