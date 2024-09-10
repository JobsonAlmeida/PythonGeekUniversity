#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Conhecendo o Pickle

A fun��o do Pickle � realizar o seguinte processo:

Objeto Python -> Binariza��o

Binariza��o -> Objeto Python

Este processo � chamado de serializa��o/deserializa��o

#OBS: O m�dulo Pickle n�o � seguro contra dados maliciosos e deste forma
n�o � recomendado trabalhar com arquivos pickle vindos de outras pessoas
que voc� n�o conhe�a ou de fontes desconhecidas.

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

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.__nome} est� comendo...")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self._Animal__nome} est� miando...")

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} est� latindo...")


felix = Gato("F�lix")
pluto = Cachorro("Pluto")

with open("animais.pickle", 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)

with open("animais.pickle", 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato chama-se {gato.nome}")
    gato.mia()
    print(f"O tipo do gato � {type(gato)}")
    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.late()
    print(f"O tipo do cachorro �{type(cachorro)}")


