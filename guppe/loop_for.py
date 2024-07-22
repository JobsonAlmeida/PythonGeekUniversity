"""
Loop for

Loop -> estrutura de repetição
for-> é uma dessas estruturas

em C
for(int i=0; i<10; i++){
//corpo do loop

}

Python
for item in interavel:
    //execução do loop

utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplo de iteraveis
- string
  nome = 'Geek University'
- listas
  lista = [1, 3, 5, 7, 9]
- range
  number  = range
"""

nome = "Geek University"
lista = [1, 2, 3, 4, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

print("\n")

for num in lista:
    print(num)

print("\n")

"""
range(valor_inicial, valor_final)
obs.: o valor_final não é inclusive
"""
for num in range(1, 10):
    print(num)

for i  in range(1, 15):
    print(nome[i])

print("-----------------")
for i, v in enumerate(nome):
    print(i, v)

"""
Obs.: Quando não precisamos de um valor, podemos descartá-lo utilizandoum underline (_)
"""
for _, v in enumerate(nome):
    print(v)

qtd = int(input("Quantas vezes esse loop deve rodar? "))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

nome = "Geek University"

for letra in nome:
    print(letra, end="")

#Original: U+1F60D
#Modificado: U0001F60D

emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60B' * num)

