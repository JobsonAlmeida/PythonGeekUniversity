#!/usr/bin/python
# -*- coding: latin-1 -*-

import math

def circunferencia(raio):
    # type: (float) -> float #type hiting em comentário
    return 2 * math.pi * raio

print(circunferencia(8))

print(circunferencia(10))

def cabecalho(texto, alinhamento=True):
    # type (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho("re", True)

def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto="42", alinhamento=True)

nome = "Geek university" #type: str

