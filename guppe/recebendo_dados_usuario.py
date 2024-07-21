
# Entrada de dados

# input() -> Todo dado recebido via input é do tipo string
"""
Em python, string é tudo que estiver entre

aspas simples ' Angelina Jolie'
aspas duplas " Angelina Jolie"
aspas triplas simples ''' Angelina Jolie '''
"""
# aspas simples duplas """ Angelina Jolie  """


print("Qual é o seu nome? ")
nome = input("Qual é o seu nome? ")

# exemplo de print antigo 2.x
#print("Seja bem-vindo(a) %s" % nome)
#print("Seja bem vindo(a) {0}".format(nome) )

#Exemplo de print mais atual
print(f'Seja bem vindo(a) {nome}')


print("Qual a sua idade? ")
idade = input("Qual a sua idade? ")

idade2 = 20

# saída de dados
#print('A %s tem %s anos' %(nome, idade2))
#print("A {0} tem {1} anos".format(nome, idade))
print(f'A {nome} tem {idade} anos')

# int(idade) => cast
# cast é a conversão de um tipo de dado em outro
print(f'A {nome} nasceu em {2018 - int(idade)}') # int(idade) => cast

