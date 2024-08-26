"""
Módulo Random e o que são módulos?

 - Em Python, módulos nada mais são do que outros arquivos Python

pacote  - grupo de módulos

importar -> o módulo já está instalado na nossa máquina. Importar então sigifica incluí-lo em nosso projeto
instalar -> o módulo não está na nossa máquina. Precisamos, colocá-lo na nossa máquina para então
depois conseguirmos importá-lo

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório

random() -> gera um número real pseudo-aleatório entre 0 e 1
não confunda a função random com o pacote random. Pode parece confuso, mas a função random é apenas uma
função dentro do módulo random
uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos
randint() -> Gera um número inteiro pseudo-aleatório entre os valores estabelecidos
choice() -> mostra um valor aleatório entre um iterável
shuffle() -> tem a função de embaralhar dados

"""

# Existem duas formas de de utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo
# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (ficarão em memória)
# Não é recomendado. Caso você saiba quais funções você precisa utilizar  deste módulo, então esta não seria a
# forma ideal de utilização.

import random

# random() -> gera um número real pseudo-aleatório entre 0 e 1
# não confunda a função random com o pacote random. Pode parece confuso, mas a função random é apenas uma
#função dentro do módulo random

print(random.random())

# Forma 2 - Importando uma função específica do módulo - forma recomendada
# Neste import estamos falando: do módulo random, importe a função random

from random import random

for i in range(10):
    print(random())

# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5,10)) # O 10 não é incluído

print("----------------")

# randint() -> Gera um número inteiro pseudo-aleatório entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1,61), end=" ")


print("\n----------------")

# choice() -> mostra um valor aleatório entre um iterável

from random import choice

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))
print(choice("Geek University"))

# shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ["K", "Q", "J", "A", "2", "3", "4", "5", "6", "7"]
print(cartas)
shuffle(cartas)
print(cartas)