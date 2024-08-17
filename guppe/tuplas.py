"""

Tuplas (tuples)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis. Isso significa que ao se criar uma tupla ela não muda. Todas operação em uma tuplas 
gera uma nova tupla



"""


print(type( () ) )


# Cuidado 1: as tuplas são representadas por parênteses

tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5

print(type(tupla1))

# Cuidado 2: Tuplas com 1 elemento

tupla3= (4)
print(type(tupla3))

tupla4= (4,)
print(type(tupla4))

tupla5= 4,
print(type(tupla5))

#Conclusão: podemos concluir que tuplas são definidas pela vírgula e não pelo uso dos parênteses

tupla = tuple(range(11))

print(tupla)
print(type(tupla))

#Desempacotamento de tupla

tupla = ("Geek university", "Programação em Python: Essencial")

escola, curso = tupla
print(escola)
print(curso)

#Observação: Gera erro se colocarmos um número diferente para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem dado o fato das tuplas serem imutáveis

# Se os valores forem inteiros ou reais sum, max, min. E len com qualquer valor

tupla = 1, 2, 3, 4, 5, 6, 7

print(sum(tupla)) 
print(max(tupla))
print(min(tupla))
print(len(tupla))

#Concatenação de tuplas

tupla1 = 1, 2, 3
print(tupla1)

tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobreescrever seus valores. Não é bloquado para re-escrita

print(tupla1)

# Podemos verificar se determinado elemento está contido na tupla

tupla = 1, 2, 3

print(3 in tupla)
print(4 in tupla)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla =  ('a', 'b', 'c', 'd', 'a', 'b')

print(tupla.count('c'))

escola = tuple("Geek University") #Convertendo string para tupla
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempres que não precisarmos modificar os dadoscontidos em uma coleção

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print(meses)

# O acesso de elementos de uma tupla é semelhante a de uma lista

print(meses[5])

# Iterar com o while

i=0
while i< len(meses):
    print(meses[i])
    i = i+1

# Verificando em qual índice um elemento está na tupla
print(meses[6]) # Here we have the indice and we want to obtain the value
print(meses.index("Julho")) # Here we have the value and we want to obtain the index
# print(meses.index("Julha")) If the element is not present into the list an error is launched
print("Julho" in meses) # Here we just want to check if the element is present into the tuple


#Obs: Caso o elemento não exista na tupla, será lançado um erro (ValueError). 

# Slice

#tupla[inicio: fim: passo]

print(meses[0: ])
print(meses[5: ])
print(meses[5: 9])

# Por que utilizar tuplas 

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro. Isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outras

tupla = 1, 2, 3

nova = tupla

print(tupla)
print(nova)

outra = 4, 5, 6

nova = nova + outra

print(nova)


