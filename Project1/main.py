#!/usr/bin/python
# -*- coding: latin-1 -*-

# video link
# https://www.youtube.com/watch?v=A7S_RwWcrK0

from datetime import datetime, timedelta

# data

hoje = datetime.now()
print(type(hoje))
print(hoje.date())
print(hoje.hour)

# variação de data
amanha = hoje + timedelta(days=1)

print(amanha)

#

data_contrato = datetime(year=2024, month=9, day=21)

atraso = data_contrato - hoje
print(type(atraso))
print(atraso.days)

# Extrair datas em outros formatos

data_contrato = "21 - 09 - 2024"

data_contrato = datetime.strptime(data_contrato, "%d - %m - %Y")
print(type(data_contrato))
print(data_contrato)

# formato brasileiro
print("--- formato brasileiro ---")
data = hoje.strftime("%d/%m/%Y")
print(data)

#fuso horário

# hoje = hoje - timedelta(hours=1)
# print(hoje)

import zoneinfo

# print(zoneinfo.available_timezones())

zona = zoneinfo.ZoneInfo("Singapore")

agora_singapore = hoje.astimezone(zona)
print(agora_singapore)