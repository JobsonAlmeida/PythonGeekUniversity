"""

Conjuntos

 - Conjuntos em qualquer linguagem de programação estamos fazendo referência à teoria dos conjuntos em matemática

 - Chamamos conjuntos ou sets (inglês)


 - Sets (conjuntos) não possuem valores duplicados
 - Sets (conjutnos) não possuem valores ordenados
 - Elementos não são acessados via indice. Ou seja, conjuntos não são indexados 

 conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles, quando não 
 precisamos se preocupar com chaves, valores e itens duplicados

 Os conjuntos (sets) são referenciados em Python com chaves {}

 Diferenças entre conjuntos e mapas (dicionários) em Python

 - Um dicionário tem chave/valor;
 - um conjunto tem apenas valor;

"""


# Definindo um conjunto

# Forma 1

s = set({1,2,3,4,5, 5, 6 ,6 , 6, 7})

print(s)
print(type(s))

# Obs.: Ao criar um conjunto, caso seja adicionaod um valor já existente, o mesmo setá ignorado sem gerar erro e não fará
# parte do conjunto

# Forma 2 = mais comum

s = {1, 2, 3, 4, 5, 5, 5, 6, 6, 7}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Iportante lembrar que além de não termos valores duplicados, também não temos ordem

lista = [15, 25, 45, 8, 58, 56, 75, 25, 8, 8 ,8 , 58, 58]
print(lista)

tupla = 15, 25, 45, 8, 58, 56, 75, 25, 8, 8 ,8 , 58, 58
print(tupla)

dicionario = {}.fromkeys(lista, 'dict')
print(dicionario)

s = {15, 25, 45, 8, 58, 56, 75, 25, 8, 8 ,8 , 58, 58}
print(s)

print(lista.__len__())

# Assim como todo outro container python, podemos colocar tipos de dados misturados em sets

s = {1, 'b', True, 34.22, 44, "String"}
print(s)
print(type(s))

for valor in s:
    print(valor)

# Usos interessantes

# cadastro de visitantes

cidades = ["São Paulo", "Campo Grande", "Cuiaba", "Campo Grande", "São Paulo", "Cuiaba"]

print(cidades)
print(len(cidades))

print(len(set(cidades)))

# Adicionando elementos in um conjunto

s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente é ignorado e não é adicionado
print(s)

# Forma 1

s.remove(3) # Não é índice! Informamos o valor a ser removido. Lembrando que nem pode ser índice porque conjuntos não são indexados
#s.remove(33) # Caso o valor não for encontrado, um erro KeyError é gerado

s.discard(2)
ret = s.discard(22) # Com o método discard, se valor não for encontrado, nenhum erro é gerado. None é sempre retornado 
print(ret)
ret2 = s.discard(1) 
print(ret2)
print(s)

novo = s.copy()
print(novo)

novo.add(44)

print(novo)
print(s)

# Podemos remover todos os intem de um conjunto

s.clear()
print(s)

# Métodos matemáticos de conjuntos

estudante_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
estudante_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}

# Conjunto com estudantes únicos

#Forma 1 - Utilizando union

unicos1 = estudante_python.union(estudante_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |

unicos2 = estudante_python | estudante_java
print(unicos2)

# Conjunto de estudantes que estão em ambos os cursos

ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudante_python & estudante_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)

# Soma, valor máximo, valor mínimo, tamanho

s= {1,2,3,4,5,6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
