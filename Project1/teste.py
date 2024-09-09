#!/usr/bin/python
# -*- coding: latin-1 -*-

# arq = open("arquivo-teste5.txt", "w")
# arq.write("Primeiro teste")
#
# entrada = input("esperando....")
#
# arq.close()

# arq = open("arquivo-teste5.txt", "r")
# dado = arq.read(1)
# print(dado)
# dado = arq.read(1)
# print(dado)
# dado = arq.read(1)
# print(dado)
# dado = arq.read(1)
# print(dado)
#
# entrada = input("esperando....")
#
# arq.close()

#
# try:
#     arq = open("arquivo-teste5.txt", "r+")
# except:
#     print("Não foi possível abrir o arquivo.")
#
# arq.seek(0)
# print(arq.tell())
# s = arq.read(1)
# print(arq.tell())
# print(s)
#
# arq.seek(0)
# arq.write("##")
#
# arq.seek(0)
# s = arq.read()
# print(s)
#
# arq.close()

# print("Escrevendo o dado no arquivo")
#
# try:
#     arq = open("arquivo-teste5.txt", "wb")
# except:
#     print("Não foi possível abrir o arquivo!")
#
# numero = 100000
#
# # arq.write(numero)
#
# bin = numero.to_bytes(4, byteorder="big", signed=True)
#
# print(bin)
# arq.write(bin)
#
# arq.close()
#
# print("Lendo o dado do arquivo")
#
# try:
#     arq = open("arquivo-teste5.txt", "rb")
# except:
#     print("Não foi possível abrir o arquivo!")
#
# x = arq.read(4)
#
# print(x)
# x_convertido = int.from_bytes(x, byteorder='big', signed=True)
# print(x_convertido)
#
# arq.close()


# Playlist used. It was seen the lesson 15.x which are about files
# https://www.youtube.com/playlist?list=PLuARAw3cqFRA7cW0zNs5fGs4989Gt9Zub
import pickle

lista = [1,2,3,4,5]

x = pickle.dumps(lista)
print(x)

y = pickle.loads(x)
print(y)

# O método dumps apenas serializa um objeto
# O método dump serializa e já armazena o dado serializado em um arquivo que deseamos informar

import pickle

try:
    arq = open("arquivo-teste5.txt", "wb")
except:
    print("Problemas com o arquivo!")

lista = [1,2,3]
pickle.dump(lista, arq)

arq.close()

import pickle

try:
    arq = open("arquivo-teste5.txt", 'rb')
except:
    print("Problemas com o arquivo!")

l = pickle.load(arq)
print(l)

arq.close()

# Mesmo utilizando a bilbioteca pickle, ainda precisamos saber a estrutura do arquivo para conseguir
# lê-lo corretamente.