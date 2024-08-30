"""
Geradores

Geradores (Generators) são Iteradores (Iterators)

Obs.: o contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Generators podem ser criados com funções geradoras
Funções geradoras utilizam a palavras reservada yield
Generators podem ser criados com Expressões Gerdoras

Diferenças entre Funções e Functions Generators (Funções Geradoras)

Funções                                       Generator Functions
utilizam return                               utilizam yield
retorna uma vez                               pode utilizar yield multiplas vezes
quando executada, retorna um valor            quando executada, retorna um generator (por isso é função geradora)

"""

# # Exemplo de Função Geradora (Generator Function)
#
def conta_ate(valor_maximo):
    contador = 1
    while contador <=valor_maximo:
        yield contador
        contador = contador + 1

# Obs: Um Generator Function não é um Generator. Ela retorna um generator.

# gen = conta_ate(5)
# print(type(gen))
#
# print(type(next(gen)))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


gen = conta_ate(10)

# for num in gen:
#     print(num)

print(next(gen))
print("Geek")
for num in gen:
    print(num)

gen = list(conta_ate(10))
print(gen)
