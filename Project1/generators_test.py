# def get_values():
#     yield "hello"
#     yield "world"
#     yield 123
#     return 42
#
# gen = get_values()
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# class IteradorHttp():
#     def __init__(self):
#         self.registro = open(‘acessos.log’, ‘r’)
#         self.linha_atual = ‘’
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.linha_atual = self.registro.readline()
#         while self.linha_atual and not self.linha_atual.startswith(‘http://’):
#             self.linha_atual = self.registro.readline()
#         if self.linha_atual:
#             return self.linha_atual
#         raise StopIteration
#
# iterador = IteradorHttp()
#
# print(next(iterador))
# print(next(iterador))

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.menor < self.maior:
    #         numero = self.menor
    #         self.menor = self.menor+1
    #         return numero
    #     raise StopIteration ("Afafadfa")

con = Contador(1, 6)

for num in con:
    print(num)
