#!/usr/bin/python
# -*- coding: latin-1 -*-

def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente s� vive uma vez.'

    return f'Estou comendo {comida} porque {final}'



def dormir(num_horas):
    if num_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado ap�s dormir por {num_horas} horas. :('



def eh_engracada(pessoa):
    # comediantes = ['Jim Carrey', 'Bozo']
    # if pessoa in comediantes:
    #     return True
    # return False
    pass