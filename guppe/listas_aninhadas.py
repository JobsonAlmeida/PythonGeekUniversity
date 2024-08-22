"""
Listas Aninhadas (Nested Lists)

 - algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - podem ser unidimensionais (arrays/vetores)
    - multidimensionais (matrizes)

Em Python nós temos as listas


numeros = [1, 'b', 3.24, True, 5]

"""

#Exemplos

listas = [[1,2,3], [4,5,6], [7,8,9]] #Matriz 3x3


print(listas)
print(type(listas))

print(listas[0])
print(listas[0][1])

print("----------------")
# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)


print("----------------")

# Iterando uma lista aninhada com List Comprehension
listaPrint = [[print(valor) for valor in lista] for lista in listas]

print("listaPrint:")
print(listaPrint)

print("----------------")

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogada para o jogo da velha 

velha = [ ['X' if numero %2 == 0 else '0' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

# Gerando valores iniciais


print([['*' for i in range(1,4)] for j in range(1,4)])