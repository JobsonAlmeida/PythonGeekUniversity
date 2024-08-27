"""
Modos de Abertura de Arquivo

r-> Abre para leitura - (padrão)
w -> Abre para escrita - tem o porém de que sobrescreve caso o arquivo já
exista
x -> abre para escrita somente se o arquivo não existir
a -> abre para escrita adicionando o conteúdo ao final do arquivo sempre. Não é  possível
 controlar o cursos com o arquivo aberto no modo a. Se o arquivo não existir, será criado.

+ -> abre uma arquivo para atualização para leitura e escrita. Não utilizamos sozinho.

"""
#
# try:
#     with open("university.txt", "x") as arquivo:
#         arquivo.write("Teste de conteudo\n")
# except:
#     print("Arquivo já existe!")
#
# with open("frutas.txt", "a") as arquivo:
#     while True:
#         fruta = input("Informe uma fruta ou sair: ")
#         if fruta != "sair":
#             arquivo.write(fruta)
#             arquivo.write("\n")
#         else:
#             break

with open("outro.txt", "r+") as arquivo:
    arquivo.seek(0)
    arquivo.seek(0)
    arquivo.write("Adicionada Mais um \n")
    arquivo.write("Outro2 De novo\n")
    # arquivo.write("Outro2 TTT\n")
