"""
Escrevendo um iterador customizado


"""

# for n in range(11):
#     print(n)
#

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor+1
            return numero
        raise StopIteration ("Afafadfa")


con = Contador(1, 6)

it = iter(con) # Podemos criar um iterator a partir de qualquer objeto que tenha o método __iter__
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# O objeto criado a partir da classe contador tem o método __iter__, logo pode ser criado um iterator
# a partir dele e assim ele pode ser usado em qualquer lugar que requisita ser criado um iterator.
# Com o iterator criado a função next será chamada em cada iteração.
# O laço for cria automaticamente o iterator a partir da classe Contador e chama a função next
# automaticamente também.
for n in Contador(1,61):
    print(n)
