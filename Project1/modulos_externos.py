"""
Módulos Externos

Utilizamos o gerenciador de pacotes pip (python installer package)


Você pode conhecer todos os pacotes externos oficiais em https://pypi.org

colorama -> é um pacote utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo

pip install nome_do_modulo

"""

from colorama import init, Fore

init()

print(Fore.RED + "Geek University")
print("ABCs")

import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)