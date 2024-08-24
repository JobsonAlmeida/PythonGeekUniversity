"""
Len, Abs, Sum, Round

len() -> retorna o tamanho (numero de itens)de um iterável

abs() -> retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real 
sem o sinal

sum -> recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial 

obs.: O valor inicial default é zero

round -> retorna um numero arrendondado para n digito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro mais próximo da entrada

"""

print(len("Geek university"))
print(len([1,2,3,4,5,6]))
print(len((1,2,3,4,5,6)))

# Pode debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte
# Dunder len
print("Geek University".__len__())

# Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5], 3))
print(sum([1,2,3,4,5], -3))
print(sum((1,2,3,4,5), 3))
print(sum((1,2,3,4,5), -3))
print(sum({1,2,3,4,5}, 3))
print(sum({1,2,3,4,5}, -3))

print(sum({'a':1, 'b':2,'c':3,'d': 4,'e': 5}.values(), 3))

# Round
print("----- round -----")
print(round(10.2))
print(round(10.49))
print(round(10.6))
print(round(102.21212121, 2))
print(round(1.299999, 2))






