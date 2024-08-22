"""
Dictionary Comprehension

Sintaxe

{chave:valor for valor in iteravel }
{valor geral desintegrado em chave:valor for valor_geral in iteravel }
o valor desintegrado no dictionary comprehension tem que quer os dois pontos separando chave e valor

"""

# Exemplos:

numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

quadrado = {chave: valor**2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1,1,3, 3, 3, 4,5]

quadrados = {valor: valor**2 for valor in numeros}
print(quadrados)

chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional

numeros = [1,2,3,4,5]

res = { num: ('par' if num%2 ==0 else 'ímpar') for num in numeros} 