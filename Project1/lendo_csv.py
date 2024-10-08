"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", 'ciência", "dados"

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; 'ciência"; "dados"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python" 'ciência" "dados"

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader


with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
"""


# with open("lutadores.csv", encoding="utf8") as arquivo:
#     dados = arquivo.read()
#     print(type(dados))
#
#     dados = dados.split(',')[2:]
#     print(dados)

# Reader

# A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:
#     - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
#     - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;


from csv import reader

with open("lutadores.csv", encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')
    next(leitor_csv) # Pular o cabeçaçho
    print(type(leitor_csv))
    for linha in leitor_csv: # Cada linha é umas lista
        print(linha)
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}')

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv: # Cada linha é um OrderedDict
        print(linha)
        print(f"{linha['Nome']} nasceu no {linha['País']} e mede {linha['Altura (em cm)']}")

