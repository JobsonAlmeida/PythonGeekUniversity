"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

"""

class Pessoa:

    def __init__(self, nome, data_nascimento, email):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def get_email(self, email):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def print(self):
        print(f"Nome: {self.__nome}\nData de nascimento: {self.__data_nascimento}\nEmail: {self.__email}")


pessoa1 = Pessoa("Jose da Silva", "29/11/1988", "jose@gmail.com")

pessoa1.print()
