"""
Pacotes

Módulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos

Pacote -> é um diretório contendo uma coleção de módulos

Obs.: Nas versões 2.3 um pacote python deveria conter dentro dele um arquivo chamdado __init__.py. Nas versões
3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para
manter compatibilidade. Com a presença do arquivo __init__ as versõs 2.x conseguem saber que o diretório
no qual este arquivo está inserido é um pacote

"""

from geek import geek1, geek2
from geek.university import geek3, geek4

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4


print(geek1.pi)
print(geek1.funcao1(4,6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())

print(funcao1(6,9))
print(funcao4())



