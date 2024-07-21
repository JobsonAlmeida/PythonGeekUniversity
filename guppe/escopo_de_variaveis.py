"""
Escopo de variáveis

Dois casos de escopo

1 - Variáveis globais
     - são reconhecidas em todo o programa, logo seu escopo compreende todo o programa

2 - Variáveis locais
    - são reconhecidas apenas no bloco onde foram declaradas, logo seu escopo compreende apenas o bloco

Python é uma linguagem de tipagem dinâmica


"""

numero = 2

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)