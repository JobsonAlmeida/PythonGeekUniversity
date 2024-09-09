#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos e deste forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas.

# Fazendo a escrita em arquivos pickle


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""


import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self._Animal__nome} está miando...")

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self._Animal__nome} está latindo...")


felix = Gato("Félix")
pluto = Cachorro("Pluto")

with open("animal.pickle", 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
