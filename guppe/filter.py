"""
Filter

A função filter serve para filtrar dados de uma dt

"""

valores = 1,2,3,4,5,6

media = sum(valores)/len(valores)

print(f"Média: {media}")


print("--- filter ---")
#Biblioteca para trabalhar com dados estatíticos
import statistics


# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f"Média: {media}")

# Assim como a função map, a função filter recebe dois parâmetros, sendo uma função e um iterável 
res = filter(lambda x: x>media, dados)
print(res)
print(type(res))

print(list(res))
print(list(res))

# Assim como na função map, após o objeto filter, que é retornado pela função filter, ser utilizado esse objeto
# é zerado

paises = [" ", "Argentina", "", "Brasil", "Chile", "", "Colombia", "Equador", "", "", "Venezuela"]

print(paises)

res = filter(lambda x: len(x) > 0, paises )
# res = filter(lambda x: x  > 0, paises )

print(list(res))

print("---- lista tweets ---- ")

# A diferença entre map e filter

# map recebe dois parâmetros e 


usuarios = [
    {
        "username": "samuel",
        "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]
    },
    {
        "username": "carla",
        "tweets": ["Eu gosto de pizzas"]
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

print(usuarios)

def verifica(dado):
    if(len(dado["tweets"]) != 0):
        return True
    else:
        return False


print("--- usuarios não inativos ---")
usuarios_nao_inativos = filter(lambda dado: len(dado["tweets"]), usuarios)

print(list(usuarios_nao_inativos))

print("--- usuarios inativos ---")

usuarios_inativos = filter(lambda dado: not len(dado["tweets"]), usuarios)
print(list(usuarios_inativos))

print(" ------------------------ ")
# Combinar filter e map
# Exemplo: Devemos criar uma lista conttendo "Sua isntrutora é + nome ", desde que o nome tenha menos
# de 5 caracteres

nomes = ["Vanessa", "Ana", "Maria"]

lista = list(map( lambda nome: f"Sua instrutora é {nome}" , filter(lambda nome: len(nome)< 5, nomes)))
print(lista)