"""
O bloco with


O bloco with é utilizado para criar um contexto de trabalho onde os recursos são abertos para serem utilizados
e são fechado automaticamente após o bloco with

É a forma que os programadores pythons gostam de trabalhar com arquivos
"""

with open("texto.txt") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
print(type(arquivo))

print(arquivo.readlines()) # O arquivo aqui está fechado