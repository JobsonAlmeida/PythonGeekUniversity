
"""
Mapas -> Conhecidos em python como dicionários

Dicionários em Python são representados por chaves {}


"""

# Acessando as chaves

receita = {'jan': 1000, 'fev': 250, 'mar': 400}

print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for value in receita.values():
    print(value)

# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma, valor máximo, valor mínimo, Tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
