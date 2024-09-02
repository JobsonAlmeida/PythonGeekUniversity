"""
Preservando metadata com wraps

Metadatas -> São dados intrísecos entre arquivos

wraps -> são funções que envolvem elementos com diversas finalidades

"""

# # Problema
#
# def ver_log(funcao):
#     def logar(*args, **kwargs):
#         """Eu sou uma funcao(logar) dentro de outra"""
#         print(f"Você está chamando: {funcao.__name__}")
#         print(f"Aqui a documentação: {funcao.__doc__}")
#         return funcao(*args, **kwargs)
#     return logar
#
# @ver_log
# def soma(a,b):
#     """Soma dois números"""
#     return a+b
#
# # print(soma(5,2))
#
# print(soma.__name__)
# print(soma.__doc__)


# Solução do problema - Apenas adicionamos o decorator wraps na funcao
# A função desse decorator wraps é preservar os metadados da função enviada para ser decorada

from functools import wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao(logar) dentro de outra"""
        print(f"Você está chamando: {funcao.__name__}")
        print(f"Aqui a documentação: {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a+b

# print(soma(5,2))

print(soma.__name__)
print(soma.__doc__)
print(help(soma))
