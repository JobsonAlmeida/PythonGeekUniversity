"""

Try/Except

E outras linguagens de programação as palavras são try/catch, mas no Python as palavras são try/except

Utilizamos o bloco try/except para tratarmos erros que podem ocorrer no nosso código. Prevenindo assim
que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é

try:
    //execução de código

except:
    //o que deve ser feito em caso de problemas


"""


# # Exemplo 1 - Tratando um erro genérico
#
# try:
#     geek()
# except:
#     print("Deu algum problema")
#
# # Tente executar a função geek(). Caso você encontre erros, imprima a mensagem de erro

# Exemplo 2

# try:
#     len(5)
# except:
#     print("Deu algum erro")

# Obs.: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre
# tratar de forma específica


# Exemplo 3 - Tratando erro de forma específica

# try:
#     len(5)
# except TypeError as err:
#     print(f"A aplicação gerou o seguinte erro: {err}")

# # Podemos efetuar diversos tratamentos de erros de uma vez
# try:
#     # len(5)
#     # geek()
#     print("geek"[9])
# except NameError as erra:
#     print(f"Deu NameError: {erra}")
# except TypeError as errb:
#     print(f"Deu TypeError: {errb}")
# except:
#     print("Deu um erro diferente")

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}
print(pega_valor(dic, 8))