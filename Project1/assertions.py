#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Assertions (Afirma��es/Checagens/Questionamentos)


Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirma��es utilizadas nos testes.

Utilizamos o 'assert' em uma express�o que queremos checar se � v�lida ou n�o.
Se a express�o for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: N�s podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada/

# OBS: A palavra 'assert' pode ser utilizada em qualquer fun��o ou c�digo nosso....n�o precisa
ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o par�metro -O, nenhum assertion
ser� validado. Ou seja, todas as suas valida��es j� eram.

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos n�meros precisam ser positivos'
    return a + b


# print(soma_numeros_positivos(10, -20))
#
# ret = soma_numeros_positivos(2, 4)  # 6
ret = soma_numeros_positivos(-2, 4)  # AssertionError
print(ret)
#
#
def comer_fast_food(comida):

    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'

    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

#
# # ALERTA: Cuidado ao utilizar 'assert'
#
#
# def faca_algo_ruim(usuario):
#     assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins!'
#     destroi_todo_o_sistema()
#     return 'Adeus'
