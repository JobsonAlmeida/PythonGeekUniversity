"""
Seek e cursors

seek() -> função utilizada para movimentar o cursor pelo arquivo. Recebe um parâmetro index que indica
onde queremos colocar o cursor. Lembrar que  conteúdo do arquivo é simplesmente um texto

seek significa procurar ou buscar

readiline -> função que lê o arquivo linha a linha

readlines -> função que lê as linhas e constrói uma lista de strings em que cada linha das lista conrresponde
a uma linha do arquivo


Qunado abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamda de streaming. Ao finalizar os trabalhos com o arquivo devemos
fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # False Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()


print(arquivo.closed)  # True - Verifica se o arquivo está aberto ou fechado


print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError


"""

arquivo = open("texto.txt")
# print(arquivo.read())
# print(arquivo.read())
# print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()


arquivo.seek(22)
# print(arquivo.read())

# ret = arquivo.readline()
# print(type(ret))
# print(ret)

# linhas = arquivo.readlines()

# print(linhas)
# print(len(linhas))

arquivo = open("texto.txt")

print(arquivo.read(50)) # Podemos limitar o numero dd caracteres lidos pelo método read
print(arquivo.closed) # verifica se o arquivo está aberto ou fechado

arquivo.close()
# Fechando o arquivo evitamos vários tipos de problemas. Assim ao fechar o arquivo outro programa pode
# abrir o arquivo
print(arquivo.closed) # verifica se o arquivo está aberto ou fechado

print(arquivo.read()) # Se tentarmos ler um arquivo fechado, temos um ValueError










