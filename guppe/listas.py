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





