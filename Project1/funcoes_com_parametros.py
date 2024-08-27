"""
Funções com Parâmetros (de entrada)
"""

def quadrado(numero):
    return numero*numero

def cantar_parabéns(aniverariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva o/a {aniverariante}!")

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return(num1 + b)*msg




def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"


# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# Argumentos nomeados (keyword arguments)
#Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print("name from funcoes_comparametro: ", __name__)
if __name__ == "__main__":

    print(nome_completo("Angelina", "Jolie"))

    print(soma(2,5))
    print(multiplica(3, 8))
    print(outra(2,3, "Geek "))

    print(nome_completo(nome="Angelina", sobrenome="Jolie"))
    print(nome_completo( sobrenome="Jolie", nome="Angelina"))

    cantar_parabéns("Marcos")

    print(quadrado(7))
    print(quadrado(2))
    print(quadrado(5))

    lista = [1,2,3,4,5,6]
    tupla = (1,2,3,4,5,6)

else:
    print("O módulo funcoes_com_parametro foi importado")