"""
1. Crie um programa que.
a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere 
“0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

#a)

arquivo = open("arq.txt", 'a')

# b)

while True:
    texto = input("Digite o texto: ")

    if texto == '0':
        break;
    
    arquivo.write(texto)
    arquivo.write("\n")

# c)
arquivo.close()

# d)

arquivo  = open("arq.txt", 'r')
texto = arquivo.read()
print(texto)

arquivo.close()