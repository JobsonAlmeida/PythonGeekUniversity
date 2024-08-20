"""
**kwargs


o **kwargs exige que utilizemos parâmetros nomeados e transforma esse parâmetros extras em um dicionário


"""


def cores_favoritas(a, b, c, *args, **kwargs):

    print(args)

    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")

cores_favoritas(10, 20, 30, marcos="verde", julia='amarelo', fernanda='azul', vanessa='branco')

#Obs.: Os parâmetros *args e **kwargs não são obrigatórios 

cores_favoritas(10, 20, 30, 40)

dic = {"marcos": "abc", 'profissão': "corretor"}
lista = [10, 20, 30]

hjd = [*lista]

print(hjd)
nome = {**dic}
print(nome)


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == "Python":
        return "Você recebeu um cumprimento Pythônico Geek"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return "Não tenho certeza de quem você é"

print(cumprimento_especial())
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek="Oi"))
print(cumprimento_especial(geek="Especial"))

"""
# Nas nossas funções podemos ter nesta ordem

 - parâmetros obrigatórios
 - *args
 - parâmetros default ( que não são obrigatórios)
 - **kwargs

"""

def func1(*args, solteiro=False):
    print("func1:")
    print(solteiro)
    print("-----")

func1(True, True, True, solteiro=True)

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)

minha_funcao(18, "Joana", 10, 20, True)


def mostra_info(a, b, *args, instrutor="Geek", **kwargs):
    return [a, b, args, instrutor, kwargs ]

print(mostra_info(1, 2, 3, sobrenome="University", cargo="Instrutor"))


def mostra_info(a, b, instrutor="Geek", *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, instrutor="Ola" , sobrenome="University", cargo="Instrutor"))

# desempacotar com kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {"nome": 'Felicity', "sobrenome": "Jones"}

print(mostra_nomes(**nomes))

# Obs.: Os nomes da chave em uma dicionário devem ser o mesmo dos parâmetros da função
# O duplo asterisco desempacota chave e valor para ser passado para parâmetros obrigatórios da função 

dicionario = dict(a=1, b=2, c=3)

def soma_multplos_numeros(a,b,c):
    print(a+b+c)

soma_multplos_numeros(**dicionario)
