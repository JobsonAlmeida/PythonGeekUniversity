#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
M�todos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Hor�rio)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))


hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudan�as ocorrendo � meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()

# Os dias da semana do m�todo weekday() come�am em 0, sendo esta a segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Ter�a-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - S�bado (Saturday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())


aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Voc� nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voc� nasceu em uma ter�a-feira')
elif aniversario.weekday() == 2:
    print('Voc� nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voc� nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voc� nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voc� nasceu em um s�bado')
elif aniversario.weekday() == 6:
    print('Voc� nasceu em um domingo')

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Mar�o de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


import datetime
from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somete a hora

almoco = datetime.time(12, 30, 0)

print(almoco)


# Marcando tempo de execu��o do nosso c�digo com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
"""

import datetime

# # A diferen�a entre now e today � que com o now podemos especificar um timezone, com o today n�o podemos especificar um time zone
# agora = datetime.datetime.now()
# print(agora)
# print(type(agora))
# print(repr(agora))
#
# print("------------------------")
# hoje = datetime.datetime.today()
# print(hoje)
# print(type(hoje))
# print(repr(hoje))

# manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time() )
#
# print(manutencao)
# print(type(manutencao))
# print(repr(manutencao))

import datetime

# def formata_data(data):
#
#     if data.month == 1:
#         return f'{data.day} de Janeiro de {data.year}'
#     elif data.month == 2:
#         return f'{data.day} de Fevereiro de {data.year}'
#     elif data.month == 3:
#         return f'{data.day} de Mar�o de {data.year}'
#     elif data.month == 4:
#         return f'{data.day} de Abril de {data.year}'
#     elif data.month == 5:
#         return f'{data.day} de Maio de {data.year}'
#     elif data.month == 6:
#         return f'{data.day} de Junho de {data.year}'
#     elif data.month == 7:
#         return f'{data.day} de Julho de {data.year}'
#     elif data.month == 8:
#         return f'{data.day} de Agosto de {data.year}'
#     elif data.month == 9:
#         return f'{data.day} de Setembro de {data.year}'
#     elif data.month == 10:
#         return f'{data.day} de Outubro de {data.year}'
#     elif data.month == 11:
#         return f'{data.day} de Novembro de {data.year}'
#     elif data.month == 12:
#         return f'{data.day} de Dezembro de {data.year}'

from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))


nascimento = datetime.datetime.strptime()

import timeit

tempo = timeit.timeit('"-". ')