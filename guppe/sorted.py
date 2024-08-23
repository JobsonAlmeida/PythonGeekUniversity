"""
Sorted

Obs.: Apesar do nome, não confunda com o método sort que já estudamos em listas. O sort só funciona em lista

Podemos utilizar o sorted com qualquer iteravel 


Como o nome diz, o sorted serve para ordenar

Além disso, o método sort de listas modifica a própria lista. A função sorted não modifica o iterável que foi
passado para ser ordenado, ele gera uma lista ordenada a partir do iterável. Independentement do iterável passado
o sorted sempre gera uma lista

"""


numeros = [6,1,8,2]
print(numeros)
print(sorted(numeros))
print(numeros)

numeros = (6,1,8,2)
print(numeros)
print(sorted(numeros))
print(numeros)

numeros = {6,1,8,2}
print(numeros)
print(sorted(numeros))
print(numeros)

# Adicionando parâmetros ao sorted

print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted para coisas mais complexas

usuarios = [
    {
        "username": "samuel",
        "tweets": ["Eu adoro bolos", "Eu adoro pizzas"],
        "cor": "amarelo",
    },
    {
        "username": "carla",
        "tweets": ["Eu gosto de pizzas"],
        "cor": "preto",
        "musica": "rock",

    },
    {
         "username": "jeff",
         "tweets": []
    },
    {
        "username": "bob123",
        "tweets": []
    },
    {
        "username": "doggo",
        "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]
    },
    {
        "username": "gal",
        "tweets": []
    },
]

print(" ------ ")
print(usuarios)
print(" ------ ")
print(sorted(usuarios, key=len))
print(" ------ ")
print(sorted(usuarios, key= lambda usuario : usuario["username"]))
print(" ------ ")
print(sorted(usuarios, key= lambda usuario : usuario["username"], reverse=True))
print(" ------ ")
print(sorted(usuarios, key= lambda usuario : len(usuario["tweets"])))







