"""
Funções com Parâmetros (de entrada)
"""

def quadrado(numero):
    return numero*numero

# print(quadrado(7))
# print(quadrado(2))
# print(quadrado(5))


def cantar_parabéns(aniverariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva o/a {aniverariante}!")

# cantar_parabéns("Marcos")

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return(num1 + b)*msg

# print(soma(2,5))
# print(multiplica(3, 8))
# print(outra(2,3, "Geek "))


def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"

# print(nome_completo("Angelina", "Jolie"))

# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# Argumentos nomeados (keyword arguments)
#Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

# print(nome_completo(nome="Angelina", sobrenome="Jolie"))
# print(nome_completo( sobrenome="Jolie", nome="Angelina"))


lista = [1,2,3,4,5,6]
tupla = (1,2,3,4,5,6)
