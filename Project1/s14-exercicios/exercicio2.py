"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:

a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

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


class Agenda:

    def __init__(self):
        self.__contatos = []
    def armazenar_contato(self, contato):
        self.__contatos.append(contato)

    def remover_contato(self, contato):
        self.__contatos.remove(contato)

    def buscar_contato(self, nome):
        for indice, contato in enumerate(self.__contatos):
            if contato.get_nome() == nome:
                print(f"{nome} está no índice: {indice}")

    def imprimir_agenda(self):
        for contato in self.__contatos:
            contato.print()

    def imprimir_contato(self, indice):
        self.__contatos[indice].print()

pessoa1 = Pessoa("José Pereira", "12/03/2000", "jose@gmail.com")
pessoa11 = Pessoa("José Pereira", "12/03/2000", "jose2@gmail.com")
pessoa2 = Pessoa("Carla Aguiar", "02/08/1995", "carla@email.com")
pessoa3 = Pessoa("Marcela da Silva", "01/07/1990", "marcela@email.com")

agenda = Agenda()

agenda.armazenar_contato(pessoa1)
agenda.armazenar_contato(pessoa11)
agenda.armazenar_contato(pessoa2)
agenda.armazenar_contato(pessoa3)
agenda.imprimir_agenda()

print("-------------------")
agenda.remover_contato(pessoa11)
agenda.imprimir_agenda()
# agenda.buscar_contato("Carla Aguiar")
# agenda.imprimir_contato(1)
# agenda.imprimir_agenda()

