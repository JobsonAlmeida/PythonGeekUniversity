"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este 
arquivo possui.

"""


nome_arquivo = input("Digite o nome do arquivo: ")

arquivo = open(nome_arquivo, "r")

print(f"Número de linhas no arquivo: {len(arquivo.readlines())}")