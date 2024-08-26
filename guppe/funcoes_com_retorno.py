"""
Funcoes com retorno

"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retono de print: {ret_pr}')

# Obs.: Em python, quando uma função não retorna nenhum valor, o retorno é None 

def quadrado_de_7():
    return (7*7)

def diz_oi():
    return 'Oi'

diz_oi()


def outra_funcao():
    return 2, 3, 4, 5

print(type(outra_funcao()))

# função para jogar cara ou coroa

from modulo_random import random

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
