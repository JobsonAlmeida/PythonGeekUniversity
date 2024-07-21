"""
Tipo float

tipo real, decimal
casas decimais

Obs: o separador de casas decimais na programação éo ponto e não a vírgula

"""

#errado do ponto de vista do float mas gera uma tupla
valor = 1, 44

print(valor)

#certo do ponto de vista do float
valor = 1.44
print(valor)

print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1,44

print(valor1)
print(valor2)

print(type(valor1))
print(type(valor2))


#Podemos converter um float para um int
"""
Obs.: Ao converter valores float para inteiro, nós perdemos precisão
"""
resultado = int(valor)

print(resultado)
print(type(resultado))

#Podemos trabalhar com numeros complexos
variavel = 5j





