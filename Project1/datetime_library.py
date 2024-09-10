#!/usr/bin/python
# -*- coding: latin-1 -*-

# video link:
# https://www.youtube.com/watch?v=eBYSjP4vf_w

import datetime

data = datetime.date(2021, 7, 14)
print(data)
print(type(data))

print("-------")

print(data.ctime())

#

dia = data.day
mes = data.month
ano = data.year
# hora = data.hour

print(dia, mes, ano)

nova_data = data.replace(month=10) # Podemos alterar uma data com o m�todo replace. Veja que � alterar realmente
                                   # a data e n�o apenas incrementar uma data existente
print(data)
print(nova_data)


hoje = datetime.date.today()

print(hoje)

delta = hoje - data
print(delta)
print(type(delta))

# Lembrar que uma coisa s�o datas espec�ficas, outra coisa s�o diferen�as de data. As diferen�as de
# data podem ser adicionadas ou subtra�das com datas espec�ficas

data_futuro = hoje + datetime.timedelta(3)
print(data_futuro)


hora = datetime.time(12, 45, 23)
print(hora)

print(hora.hour)
print(hora.minute)
print(hora.second)

datatempo = datetime.datetime(2021, 4, 14, 7,18,19)
print(datatempo)

agora = datetime.datetime.now()
print(agora)

agora_string = agora.strftime("%m/%d/%Y %H:%M:%S")
print(type(agora_string))
print(agora_string)


agora_padrao = datetime.datetime.strptime(agora_string, "%m/%d/%Y %H:%M:%S")
print(type(agora_padrao))
print(agora_padrao)


