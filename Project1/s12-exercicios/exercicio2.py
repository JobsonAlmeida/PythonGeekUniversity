"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são 
vogais e quantas são consoantes.
"""

nome = input("Digite o nome do arquivo: ")

n_vogais = 0
n_consoantes = 0
for letra in nome:
    if letra in "aAeEiIoOuU":
        n_vogais = n_vogais + 1
    else:
        if(letra != "\n" and letra !=" "):
            n_consoantes = n_consoantes + 1

print(f"Número de vogais {n_vogais}")
print(f"Número de consoantes {n_consoantes}")

