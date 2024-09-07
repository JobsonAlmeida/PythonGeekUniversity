"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivaçao Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


#OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes.
"""

# Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3): # Não existe limite para a quantidade de classes herdadas em Python
    pass

# Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2): # Aqui a classe Base3 está herdando diretamente a Base2 e indiretamente a Base 1
    pass

class MultiDerivada(Base3): # Aqui está ocorrendo duas multiderivações indireta
    pass                    # A classe MultiDerivada está herdando diretamente a Base3 e indiretamente
                            # a Base2 e a Base1

#OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
# todos os atributos e métodos das super classes.

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome } está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim("Alfred")
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # A ordem da herança altera qual method cumprimentar será executado

print(f'Tux é instância de Pinguin? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')

# todas as classes do python herdam da classe object. The class creation bellow are the same:
class Pessoa:
    pass

class Pessoa(object):
    pass
