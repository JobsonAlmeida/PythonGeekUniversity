"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> cápsula



              classe
---------------------------------
|                               |
|         atributos e métodos   |
|_______________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()


Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.
"""

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):

        if valor < 0:
            print("O valor deve ser positivo")
        else:
            if self.__saldo <= valor:
               print("Saldo insuficiente para saque!")
            else:
                self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        self.__saldo -= 10 # taxa de transferência
        conta_destino.__saldo += valor

#

conta1 = Conta("Geek", 300.00, 1500)
conta2 = Conta("Felicity", 300, 2000)
#
# print(conta1.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)


# print(conta1._Conta__numero)
#
# print(conta1.depositar(-300))
# print(conta1.extrato())
# print(conta1.sacar(300))
print(conta1.__dict__)
print(conta2.__dict__)

conta1.transferir(100, conta2)

print(conta1.__dict__)
print(conta2.__dict__)