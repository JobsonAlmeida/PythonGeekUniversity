"""

PDB - Python debugger

bug -> inseto

debug -> tirar o inseto



"""
# #Obs.: Autilizaçã do print para debugar codigo é uma prática ruim.
# def dividir(a, b):
#     print(a,b)
#     try:
#         return int(a)/int(b)
#     except (ValueError, ZeroDivisionError) as err: # podemos passar um tupla especificando os tipos de erros a ser tratados
#         return f"Ocorreu um problema: {err}"

# Existem formas mais profissionais de fazer o debug utilizando o debugger
# Em python, podemos fazer isso em diferentes IDES, como o PyCharm ou utilizando o PDB (Python Debugger)

# # Exemplo com PyCharm
#
# def dividir(a, b):
#     print(a,b)
#     try:
#         return int(a)/int(b)
#     except (ValueError, ZeroDivisionError) as err: # podemos passar um tupla especificando os tipos de erros a ser tratados
#         return f"Ocorreu um problema: {err}"
#
# print(dividir(4,0))
#
# print("abc")
#
# a = 10
# b = 20
# print(dividir(a, b))


# Exemplo com o PDB - exemplo 1
# Para utilizar o Python debugger precisamos importar a bilbioteca pdb e então utilizar a função
# set_trace()

# comandos básicos do pdb
# l para listar onde estamos no código
# n próxima linha
# p imprime variável
# c continua a execução - finaliza o debugging

# import pdb
#
# nome = "Angelina"
# sobrenome = "Jolie"
# pdb.set_trace()
# nome_completo = nome + " " + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)
#
# # Exemplo com o PDB - exemplo 1
# # Para utilizar o Python debugger precisamos importar a bilbioteca pdb e então utilizar a função
# # set_trace()
#
# # comandos básicos do pdb
# # l para listar onde estamos no código
# # n próxima linha
# # p imprime variável
# # c continua a execução - finaliza o debugging


# # Exemplo com o PDB - exemplo 1
#
# nome = "Angelina"
# sobrenome = "Jolie"
# import pdb; pdb.set_trace()
# nome_completo = nome + " " + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)
#
# # Por que utilizar este formato?
# # O debug é utilizando durante o desenvolvimento. Constumamos realizar todos os imports de bibliotecas
# # no início do arquivo. Para isso, ao invés de colocarmos o import do pdb no íncio do arquivo,
# # nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção


# # A partir do Python3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# # incorporado como função built-in chamada breakpoint()
#
# # comandos básicos do pdb
# # l para listar onde estamos no código
# # n próxima linha
# # p imprime variável
# # c continua a execução - finaliza o debugging
# # p <variavel> imprime o valor da variável informada
#
# nome = "Angelina"
# sobrenome = "Jolie"
# breakpoint()
# nome_completo = nome + " " + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)
#
# # Por que utilizar este formato?
# # O debug é utilizando durante o desenvolvimento. Constumamos realizar todos os imports de bibliotecas
# # no início do arquivo. Para isso, ao invés de colocarmos o import do pdb no íncio do arquivo,
# # nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção

# Obs: Cuidado com os conflitos de variáveis e os comandos do pdb


def soma(l,n,p,c):
    breakpoint()
    return l+n+p+c

print(soma(1,3,5,7))

# Quando os nomes das variáveis são os mesmos que o comandos do pdb, podemos utilizar o comando p para
# imprimir as variáveis, ou seja, p <nome_da_variavel>

