"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o softeware precisa
ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.


StringIO ->função utilizada para ler e criar arquivos em memória. Não grava arquivo no disco.

O arquivo em memória criado pelo StringIO pode ser lido com o read e também escrito com o write


"""

from io import StringIO

mensagem = "Esta é apenas uma string normal"

# Podemos criar um arquivo em memoria já com uma string inserida ou vazio para inserirmos texto depois

arquivo = StringIO(mensagem) # Aqui não temos um nome para o arquivo
# arquivo = open("arquivo.txt", "w") #Aqui temos um nome para o arquivo

# Agora tendo o arquivo podemos utilizar tudo que ja sabemos
print(arquivo.read())

arquivo.write(" Outro texto")

arquivo.seek(0)
print(arquivo.read())


