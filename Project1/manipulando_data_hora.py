#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

2018-12-21 15:36:38.056382

2018-12-21 15:41:38.056382

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora corrente

print(datetime.datetime.now())  # 2018-12-21 15:36:38.056382   BR 21/12/2018


# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))


# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segund, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data
print(type(evento))

print(type('31/12/2018'))


print(evento)


nascimento = input('Informa sua data de nascimento (dd/mm/yyy): ')

nascimento = nascimento.split('/')


nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

# import datetime



# Quando importamos o módulo datetime temos disponível a classe datetime
# print(dir(datetime))
# print(type(datetime.datetime))
# print(type(datetime.MAXYEAR))


#
# print(datetime.MAXYEAR)
# print(type(datetime.MAXYEAR))
# print(datetime.MINYEAR)
# print(type(datetime.MINYEAR))

# print(repr(datetime.datetime.now()))


# inicio = datetime.datetime.now()
# print(inicio)
# print(type(inicio))
#
# inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
# print(inicio)


# evento = datetime.datetime(2019, 1, 1, 0)
# print(type(evento))
# print(type('31/12/2018'))
# print(evento)

# nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
# print(nascimento)
# nascimento = nascimento.split('/')
#
# nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
# print(nascimento)
# print(type(nascimento))

import datetime

evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

