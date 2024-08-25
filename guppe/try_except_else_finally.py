"""

Try / Except / Else / Finally


Dica de quando e onde tratar código

Toda entrada do usuário deve ser tratada
Toda entrada deve ser tratada

Obs.: Afunção do usuário é destruir o seu sistema

Else -> é executado somente se não ocorrer nenhum erros especificados.

Finally -> é sempre executado, independentemente se houve erro ou não
    O finally é, geralmente, utilizado para fechar ou desalocar recursos
"""

# num=0
# try:
#     num = int(input("Informe um número: ")) # Se algum erro ocorrer a variável num nunca será criada
# except ValueError:
#     print("Valor incorreto")
# except TypeError:
#     print("Tipo incorreto")
# except SyntaxError:
#     print("Ocorreu erro de sintaxe")
# else:
#     print(f"Você digitou: {num}")
# finally:
#     print("Sempre vou ser executado")


# # Exemplo mais complexos - correto
# # Você é responsável pelas entradas das suas funções. Entãom trate-as!
#
# def dividir(a, b):
#     try:
#         return int(a)/ int(b)
#     except ValueError:
#         return "Valor incorreto"
#     except ZeroDivisionError:
#         return "Não é possível realizar uma divisão por zero"
#
#
# num1 = input("Informe o primeiro número: ")
# num2 = input("Informe o segundo número: ")
#
# print(dividir(num1, num2))


# # Exemplo mais complexos - genérico
# # Você é responsável pelas entradas das suas funções. Entãom trate-as!
# # Aqui estamos tratando de forma genérica. O ideal é tratar cada erro específico
# def dividir(a, b):
#     try:
#         return int(a)/ int(b)
#     except:
#         return "Ocorreu um problema"
#
#
# num1 = input("Informe o primeiro número: ")
# num2 = input("Informe o segundo número: ")
#
# print(dividir(num1, num2))


# Exemplo mais complexos - semi-genérico
# Você é responsável pelas entradas das suas funções. Entãom trate-as!
# Aqui estamos tratando de forma genérica. O ideal é tratar cada erro específico
def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err: # podemos passar um tupla especificando os tipos de erros a ser tratados
        return f"Ocorreu um problema: {err}"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))