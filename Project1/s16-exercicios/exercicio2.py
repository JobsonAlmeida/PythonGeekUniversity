"""
2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
"""

from exercicio1 import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas

    def __str__(self):
        return f'marca: {self._Veiculo__marca}, modelo: {self._Veiculo__modelo}, portas: {self.portas}'

    def imprimir(self):
        super().imprimir() # We could use the imprimir method from the super class
        print(f'marca: {self._Veiculo__marca}, modelo: {self._Veiculo__modelo}, portas: {self.portas}')

if __name__ == "__main__":
    carro1 = Carro("Honda", "HR-V", "GHD56845")

    print(carro1)

    print(carro1.marca)
    carro1.marca = "BMW"
    print(carro1.marca)

    print(carro1.modelo)
    carro1.modelo = "Astra"
    print(carro1.modelo)

    print(carro1)
