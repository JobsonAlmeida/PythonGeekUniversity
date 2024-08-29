"""
Criando sua própria versão de loop


"""


# for num in [1,2,3,4,5]: # Por baixo do panos o pythons aplica a função iter na lista para criar um iterable
#                         # a partir da lista e aplica o next neste iterator para que seja devolvido
#                         # os elementos individuais um a um
#     print(num)
#
# for letra in "Geek University":
#     print(letra)

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for("Geek University")

numeros = [1,2,3,4,5,6]

meu_for(numeros)