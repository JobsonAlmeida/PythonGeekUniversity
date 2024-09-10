# import datetime
#
# data_hoje = datetime.datetime.now()
#
# aniversario = datetime.datetime(2018,3,3,0)
#
# tempo_para_evento = data_hoje - aniversario
#
# print(type(tempo_para_evento))
# print(repr(tempo_para_evento))
# print(tempo_para_evento)
# print(tempo_para_evento.days)
# print(tempo_para_evento.seconds/3600 )


import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
