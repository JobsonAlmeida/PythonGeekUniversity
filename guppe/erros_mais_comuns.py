"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saidas de erros geradas pele execução do nosso código


Erros mais comuns:

SyntaxError -> Ocorroe quando o Python encontra um erro de sintaxe. Ou sea, você escreveu algo
 que o Python não reconhece como parte da lingagem


"""

print("Geek University")

def funcao():
    print("Geek University")

list = 1

# def = 1

# return

# NameError -> ocorre quando uma variável ou função não foi definida

# print(geek)

# geek()

a = 80
msg = None
if a < 10:
    msg = "É menor que 10"

print(msg)

# TypeError -> ocorre quando uma funcao/operação/ação é aplicada a um tipo errado

#print(len(5)) # neste caso não podemos aplicar a função len a um valor que é do tipo int

#print("Geek" + [])

# IndexError -> ocorre quando tentamos accessar um elemento em uma lista outro tipo de dado
# indexado utilizando um índice inválido

lista = ("Geek")
# print(lista[0][10])

#ValueError -> ocorre quando uma função/operação built-in recebe um argumento com tipo correto
# mas valor inapropriado

print(int("42"))
# print(int("Geek"))

# KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe
dic = {'python': "university"}
# print(dic["geek"])

#AttributeError -> Ocorre quando uma variável não tem um atributo ou função

tupla = (11, 2, 31, 4)
# print(tupla.sort())

# IdententionError -> Ocorre quando não respeitamos a identação do Python que é de 4 espaços

# def nova():
# print("Geek")

# for i in range(10):
# i+1

# Exceptions e Erros são sinônimos na programação

