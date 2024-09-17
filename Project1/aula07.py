#!/usr/bin/python
# -*- coding: latin-1 -*-

import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = "Geek University"
nome2 = 10

peso: float = 67.9

ativo: bool

ativo = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f"{self.__nome} está andando"

p = Pessoa(nome="Geek University", idade=37, peso = 9.5)

print(p.__dict__)

# print(p.__annotations__) # O objeto não tem __annotations__
print(p.andar.__annotations__) # O método tem __annotations__

