"""
Leitura de arquivos

open() -> função integrada para abrir aquivos
Na forma mais simples de utilização recebe apenas o caminho para o arquivo. Essa função retorna um _io.TextIOWrapper

Obs.: Por padrão a função open abre o arquivo para leitura. Este arquivo deve existir ou então teremos o
erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode='r' -> indica que modo de abertura do arquivo é somente para leitura (read)
"""

arquivo = open("texto.txt")
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após a sua abertura, devemos utilizar a função read() do
# objeto '_io.TextIOWrapper' retornado pela função built-in open

ret = arquivo.read()
print(type(ret))
print(ret)
print(ret)


# print(arquivo.read())
# print(arquivo.read())

# O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona
# como o cursor quando estamos escrevendo.
# a função reado() lê todo o conteúdo do arquivo


