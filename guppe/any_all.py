"""
Any e All


all -> retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

any -> retrona true se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna false
"""

print(all([0,1,2,3,4,5,6]))
print(all([1,2,3,4,5,6]))
print(all([]))
print(all((1,2,3,4,5,6)))
print(all({1,2,3,4,5,6}))
print(all("Geek"))


print("---------------")
nomes = ["Carlos", "Camila", "Cassiano", "Cristina"]

print([nome[0] == 'C' for nome in nomes])

print(all([nome[0] == 'C' for nome in nomes]))

print([letra for letra in "eio" if letra in "aeiou"])
print(all([letra for letra in "eio" if letra in "aeiou"]))

print("---- any ----")
print(any([0,1,2,3,4,5,6]))
print(any([0,0,0,0,0,0,0]))
print(any([]))

nomes = ["Carlos", "Camila", "Cassiano", "Cristina", "Vanessa"]

print(any([nome[0] == 'C' for nome in nomes]))