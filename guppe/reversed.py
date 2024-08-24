"""
Reversed

Obs.: Não confunda com o méotodo reverse que estudamos nas listas

A função reversed funciona com qualquer iterável. Sua função é inverted o iterável.

A função reversed retorna um iterável chamado list_reverseiterator. Podemos coverter o elemento retornado para 
uma lista, tupla ou conjunto

"""

lista = [1,2,3,4,5,6]
lista.reverse()
print(lista)

lista = [1,2,3,4,5,6]
res = reversed(lista)
print(res)
print(type(res))
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # Lembrar que em conjunto a ordem não é definida

# Podemos iterar sobre o objeto retornado pela função reversed 

for letra in reversed("Geek University"):
    print(letra, end="")

#Podemos fazer o mesmo sem o uso do for
print("\n------")
print(''.join(list(reversed("Geek University"))))
print(''.join(list(reversed("Geek University"))))

# Já vimos como fazer isso utilizando o slice de strings
print("Geek University"[::-1])

# Podemos também utilizar o reversed para fazer um loop for reverso
for n in reversed(range(0,10)):
    print(n)

# Já vimos como fazer isso utilizando o próprio range
for n in range(9,-1,-1):
    print(n)