"""
3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo
"""

from exercicio2 import Carro

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

    carro1.imprimir()
