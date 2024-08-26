"""
Módulos Customizados

Como móduloa python nada mais são do que arquivos python, então todos os arquivos que criamos neste curso
são módulos Python prontos para serem utilizados


"""

# Importando uma função específica do nosso módulo
from funcoes_com_parametros import soma

print(soma(2,3))


# Importando todo o módulo (temos acesso a todos os elementos do módulo

import funcoes_com_parametros # Fazendo esse tipo de importação, estamos importando todas as funções,variáveis,
                              # objetos e etc do pacote funcoes_com_parametros, porém para utiliza-los
                              # é necessário utilizar o nome do escopo

from funcoes_com_parametros import * # Fazendo esse tipo de importação, estamos importando todas as funções,variáveis,
                              # objetos e etc do pacote funcoes_com_parametros, e para utiliza-los
                              # não é necessário utilizar o nome do escopo

print(lista)
print(tupla)

from random import * # Fazendo esse tipo de importação, para utilizar as funções não é necessário
                     # utilizar o nome do escopo. Basta apenas utilizar o nome da função.
                     # Atenção que aqui está sendo importado todas as funções

import random # Fazendo esse tipo de importação, para utilizar as funções é necessário
                     # utilizar o nome do escopo