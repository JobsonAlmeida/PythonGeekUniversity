"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
comece com o asterisco

O parãmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla. Lembre-se
de que tuplas são imutáveis

"""


# def soma_todos_numeros(num1, num2, num3):
#     return num1 + num2 + num3

# print(soma_todos_numeros(4, 6, 9))


def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

def soma_todos_numeros(nome, email, *args ):
    return sum(args)

print(soma_todos_numeros(  "faad", 'fada', 2, 5, 2, 3))

print(soma_todos_numeros("Angelina", "jolie@gmail.com", 2, 3))
# print(soma_todos_numeros(1))
# print(soma_todos_numeros(1,2))
# print(soma_todos_numeros(1,2,3))

def verifica_info(*args):
    if 'Geek' in args and "University" in args:
        return "Bem-vindo Geek!"
    return "Eu não tenho certeza de quem você é"

print(verifica_info())
print(verifica_info(1, True, "University", 'Geek'))
print(verifica_info(1, 'University', 3.14))

def soma_todos_numeros(*args ): # Here we are using the rest parameter
    return sum(args)


numeros = [1,2,3,4,5,6,7,8,9]
# O asterisco serve para informarmos ao Python que estamos passando como argumento uma coleção de dados. 
# Desta forma, ele saberá que precisará antes desempacotar este dados
print(soma_todos_numeros(*numeros)) # Here we are using the spread parameter