"""
Listas

Listas em python funcionam como vetores/matrizes/arrays em outras lignagesn com a diferença de serem DINÂMICAS e também poder colocar qualquer tipo de dado.

-Dinâmico


Linguagens C/Java os arrays:
   - possuem tamanho e tipo de dados fixos
   Ou seja, nestas linguagens se você cirar um array do tipo int e com tamanho 5, este array será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores;

Já em Python

 - Dinâmico : A lista não possui tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir acicionando elementos;
 O tamanho da lista é restrita ao tamanho da memória do computador.

 - Qualquer tipo de dados: As listas não possuem tipo de dados fixo. Ou seja podemos colocar qualquer tipo de dados

 As listas em python são representadas por colchetes: []

"""

lista1 = [99, 4, 27, 15, 89, 78, 46]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list("Geek University")

print(lista5)

#Podemos facilmente checar se determinado valor está contido na lista

num = 18
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Não encontrei o numero {num}")

#Podemos facilmente ordenar uma lista

lista1 = [1, 99, 4, 27, 15, 89, 78, 1, 46]

lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista

print(lista1.count(1))
print(lista5.count("e"))

# Adicionar elementos em listas
#Obs.: para adicionar elemtnos em listas utilizamos a função append
#Com append nós somente conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8,3,1]) #Adicionamos apenas um elemento à lista
print(lista1)
if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67]) #Adicionamos os elementos individualmente à lista. extend só aceita iteraveis e adiciona cada elemento desse iteravel à lista
print(lista1)

#Podemos inserir um novo elemento na lista informando a posição do índice
#Isso não substitui o valor inicial. O mesmo será deslocado para a direita
lista1.insert(2, "Novo valor")
print(lista1)

#Podemos facilmente juntar duas listas
lista6 = lista1 + lista2

print(lista6)

#lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista

#forma1
lista1.reverse()
lista2.reverse()


print(lista1)
print(lista2)

#forma2
print(lista1[::-1])
print(lista2[::-1])

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quanto elementos existem dentro da lista
print(len(lista1))
print(len(lista2))
print(len(lista3))

#Podemos facilmente remover o último elemento de uma lista
#O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo índic
#Obs.: Os elementos à direita desse indice serão deslocados para a esquerda
#Obs.: Se não houver elemento no índice informado teremos o erro IndexErro
lista5.pop(2)
print(lista5)

#Podemos remover todos os elementos
print("limpando a lista")
print(lista5)
lista5.clear()
print(lista5)

#Podemos facilmente repetir elementos em uma lista
print("-----")
nova = [1, 2, 3]
print(nova)
nova = nova*3
print(nova)

#Podemos facilmente converte uma string para uma lista

curso = "Programação em Python Essencial"
print(curso)
curso = curso.split()
print(curso)

#Obs.: Por padrão os split separa os elementos da lista pelo espaço entre elas

curso = "Programação,em,Python,Essencial"
print(curso)
curso = curso.split(',', 2)
print(curso)

#Convertendo uma lista em uma string
lista6 = ["Programação", "em", "python", "essencial"]
print(lista6)

#Pega a lista6 coloca um espaço entre cada elemento e transforma em uma string
curso = " ".join(lista6)
print(curso)

curso = "$".join(lista6)
print(curso)


#Podemos misturar tipos de dados colocados na lista
lista6 = [1, 2.34, True, "geek", 'd', [1, 2, 3], 828289238492492]

#Iterando sobre listas

lista1 = [1, 99, 4, 27, 15, 34, 42, 45, 55, 43 ]
print("--- iterando sobre listas ---")
for elemento in lista1:
    print(elemento)


# carrinho = []
# produto = ''
#
# while produto != 'sair':
#     print("Adicione um produto na lista ou digite 'sair' para sair: ")
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)

# Utilizand varivaveis em listas

numeros = [2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]

print(numeros)

#Fazemos acesso aos elementos de forma idexada

cores = [ "verde", 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazemos acesso aos elementos de forma indexada inversa
# Para entender o índice negativo pense na lista como um círculo onde o final está ligado ao ínicio
print(cores[-4])
print(cores[-3])
print(cores[-2])
print(cores[-1])

# # Gera erro neste caso
# print(cores[-8])
# print(cores[-7])
# print(cores[-6])
# print(cores[-5])


print("-----------------")
cores = ["verde", 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#Gerar indice em um for
cores = ["verde", 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)

print(lista)

print("---")
# Métodos não tão importantes, mas também úteis

#Encontrar o índice de um elemento na lista

numeros = [5, 6, 5, 8, 8, 3, 2, 0, 5]

print(numeros.index(6))
print(numeros.index(5))
# print(numeros.index(600)) # Se o elemento não estiver na lista é retornado um erro

# Podemos fazer busca dentro de um range, ou seja qual indice começar a buscar

print(" ----busca ----")
print(numeros.index(5, 3))

#Podemos fazer busca dentro de um range inicio e fim
print(numeros.index(6, 1, 10))

#Slicing
#lista[inicio:fim:passo]

numeros = [5, 6, 5, 8, 8, 3, 2, 0, 5]
print(numeros[0:10:2])
print(numeros)


#Trabalhando com o parâmetro início
print("---trabalhando com o parêmtro inicio----")
lista = [1,2,3,4,5,6]
print(lista[1:])
print(lista[-1:])
print(lista[-3:])

#Trabalhando com o parâmetro fim
print("---trabalhando com o parêmtro fim----")
lista = [1,2,3,4,5,6]
print(lista[:2]) #começa no início da lista (índice 0)  e vai até o índice 2-1
print(lista[:-1])
print(lista[:-3:2]) # podemos incluir um passo

#Trabalhando com o passo

print(lista[1::2]) #Começa no índice 1 e vai até o final da lista de 2 em 2
print(lista[::2]) #Começa no início da lista (índice 0) e vai até o final de 2 em 2
print(lista[2::-1]) #Começa do índíce 1 e vai até o final da lista com passo de -1.
print(lista[0::1])


#Invertendo valores em uma lista
print("---invertendo valores---")
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0] #Interesting way to change values whithout an auxiliar variable
print(nomes)

#Soma*, valor máximo*, valor mínimo*, tamanho
# Se os valores forem todos inteiros ou reais

lista = [1,2,3,4,5,6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transfomando uma lista em tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista = [1,2,3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Obs.: Se tivermos um número de elementos na lista diferente em comparação com o número de variáveis para receber os dados, recebemos um value error.

# Copiando uma lista para outra (shallow copy e deep copy)
print("---Copiando listas---")
lista = [1,2,3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

print("---fazendo a copia----")
lista1 = [1, 2, ['a', 'b'], 3, 4, 5, 6]
lista2 = lista1.copy()

print(lista1)
print(lista2)

print("--- depois  de inserir um novo elemento---")

lista1[2].append("xyz")
print(lista1)
print(lista2)












