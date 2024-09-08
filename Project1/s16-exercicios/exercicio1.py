"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.
"""

class Veiculo:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def __str__(self):
        return f'marca: {self.__marca}, modelo: {self.__modelo}'

    def imprimir(self):
        print(f'marca: {self.__marca}, modelo: {self.__modelo}')


# Testando

if __name__ == "__main__":

    veiculo1 = Veiculo("Honda", "HR-V")

    print(veiculo1)

    print(veiculo1.marca)
    veiculo1.marca = "BMW"
    print(veiculo1.marca)

    print(veiculo1.modelo)
    veiculo1.modelo = "Astra"
    print(veiculo1.modelo)

    print(veiculo1)
