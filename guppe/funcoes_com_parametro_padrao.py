""""
Funções com Parâmetros Padrão (Default Parameters)

 - Funções onde a passagem de parâmetro seja opcional

"""

print("Geek University")
print()

# def quadrado(numero):
#     return numero*2

# print(quadrado(2))


# Em funções python os parâmetros com valores default devem sempre estar ao final da declaração
def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2,3))
print(exponencial(3,2))
print(exponencial(7))
print(exponencial())

def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor"
    
    return f"Olá {nome}"

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao("Ozzy"))


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat (num1, num2, fun=soma): # Podemos passar qualquer tipo como valor padrão para o argumento, inclusive uma função 
    return fun(num1, num2)

print(mat(2,3))
print(mat(2,2, subtracao))


# Variáveis locais se sobrepoem à variáveis globais de mesmo nome
instrutor = "Geek"

def diz_oi():
    instrutor = "Python" 
    return f'Oi {instrutor}'

print(diz_oi())


print("--------------")
total = 5

def incrementa():
    # global total # Avisando que queremos utilizar a variáve global
    # total = total + 10
    return total + 2
print(incrementa())
print(total)
print(incrementa())


# Podemos ter funç~eos que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador # nonlocal indica que a variável não é local e nem global e sim a variável que está na função anterior
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

