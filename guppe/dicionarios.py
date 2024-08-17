"""
Dicionarios

Obs.: Em algumas lingaugens de programação os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave-valor

Obs.:

 - Dicionários são representados por chaves {}
 - Chave e valor são separados por dois pontos :
 - Tanto a chave quanto o valor podem ser de qualquer tipo de dado. Podemos misturar tipos de dados


"""

print(type({}))

#Criação de dicionários
#Forma 1
paises = {'br': 'Brasil', 'eua': "Estados Unidos", 'py': 'Paraguai'}

#Forma 2 (menos comum)

paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

#Caso tentamos fazer o acesso utilizando uma chave que não existe teremos o erro KeyError
# print(paises['ab'])

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ab'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado o erro KeyError
# O tipos None é sempre considerado como false
# Podemos definir um valor padrão para caso não encotremos o objeto com a chave informada
pais = paises.get('brm', "Não encontrado")

if pais:
    print(f'Encontrei o país {pais}')
else:
    print("Não encontrei o país")

print(f"Encontrei o pais {pais}")

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla, dicionarios como chaves 
#de dicionarios

#Tuplas são muito utilizadas como chaves de dicionários, pois elas são imutáveis
localidades = {
    (35.6895, 39.6917) : 'Escritório em Tóquio', 
    (40.7128, 74.0060) : 'Escritório em Tóquio',
    (37.7749, 122.4194 ) : 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

#Forma 1

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})

#conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
#conclusão 2: Em dicionários não podemos ter chaves repetidas

# Remover dados de um dicionário
# 
# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# Obs: precisamos sempre informar a chave e caso não encontre o elementos um KeyError é retornado.

#Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
#Neste caso o valor removido não é retornado
# del receita['fev']

# Imagine que você tem um comércio eletrônico onde temos um carrinho de compras na qual adicionamos produtos

"""
Carrinho de compras
Produto 1:
    - nome;
    - quantidade;
    - preço;
`Produto 2:
    - nome;
    - quantidade;
    - preço;
"""

# Poderíamos utilizar uma lista para isso

carrinho = []

produto1 = ["Playstation", 1, 2300.00]
produto2 = ["God of War", 1, 150]

carrinho.append(produto1)
carrinho.append(produto2)

# Teríamos que saber qual é o índice de cada informação no produto

# Poderíamos utilizar uma tupla

produto1 = ('Playstation4', 1, 2300.00)
produto2 = ("God of War", 1, 150)

carrinho = (produto1, produto2)

print(carrinho)

# Poderíamos utilizar um dicionário para isso

carrinho = []

produto1 = {'nome': "Playstation 4", 'quantidade': 1, 'preço':2300.00}
produto1 = {'nome': "God of War", 'quantidade': 1, 'preço':150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemoster a certeza sobre cada informação

 # Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

d.clear()

print(d)

#Copiando um dicionário para outro

# Forma 1

d = dict(a=1, b=2, c=3)

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmentros: um iterável e um valor. Ele vai gerar para cada valor do iterável 
# uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)