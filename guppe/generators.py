"""
Generators

Em aulas anteriores nós estudamos

 - list comprehension
 - dictionary comprehension
 - set comprehension  

 Não vimos tuple comprehension -> por que elas se chamam generators

 O generator é semrpre mais performático que o list coprehensio, dictionary comprehension e set comprehension

 O generator não coloca os dado em memória. Ele só ira gerar os valores quando você for utilizar. 

"""
nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristiana", "Vanessa"]

# como list comprehension
res = [nome[0]=="C" for nome in nomes]
print(res)

# como generator
res = (nome[0]=="C" for nome in nomes)
print(type(res))

from sys import getsizeof


# Mostra quantos bytes a string Geek está ocupando em memória
print(getsizeof("Geek"))
print(getsizeof("University"))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(923554875))
print(getsizeof(True))

# gerando uma lista de números com list comprehension

list_comp = getsizeof([x*10 for x in range(1000)])
ser_comp = getsizeof({x*10 for x in range(1000)})
dict_comp = getsizeof({x: x*10 for x in range(1000)})

# gerando um lista de numeros com generator

gen = getsizeof(x*10 for x in range(1000))

# Para fazer a mesma tarefa gastamos em memória 
print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {ser_comp} bytes")
print(f"Dictionary Comprehension: {dict_comp} bytes")
print(f"Generator: {gen} bytes")


gen = (x*10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)



 