#!/usr/bin/python
# -*- coding: latin-1 -*-
# def cumprimentar(nome: str) -> str:
#     return f"Olá, {nome}"
#
# print(cumprimentar("Geek"))


# nome: str = 10

nomes: list[str] = ['Luiza', 'Henrique', 10]
print(nomes)

def cabecalho(texto: str, alinhamento : bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho("geek university"))

print(cabecalho("geek university", "geek"))

