"""
Documentando funções com Docstrings

Obs: Podemos ter acesso à documentação de uma função em python utilizando a propriedade especial __doc__

"""

# print(help(print))

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi! '

print(diz_oi())
print(help(diz_oi))


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de número ou número elevado à potência informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Portência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

print(help(exponencial))