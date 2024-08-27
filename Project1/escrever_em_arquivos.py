"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmor um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)


# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()


# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais Esta é a última linha.')


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""


# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
# caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
# o conteúdo no arquivo anterior é perdido.
with open("novo.txt", "w") as arquivo:
    a = 10
    # arquivo.write("Novos dados.\n")
    # arquivo.write("Outros  colocar quantas linhas quisermos.\n")
    # arquivo.write("Esta é a última linha.\n")

with open("geek.txt", 'w') as arquivo:
    arquivo.write("Geek"*1000)


with open("frutas.txt", 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != "sair":
            arquivo.write(fruta)
            arquivo.write("\n") # é a ação de abrir o aruivo no modo de escrita w que deleta o arquivo e cria
                                # outro novamente e não o método de escrita write. O método de escrita write
                                # apenas escreve no arquivo
        else:
            break

