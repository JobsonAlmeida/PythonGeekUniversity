"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância
e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))


print(Produto.desconto(p1, 40))  # self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f'Senha User 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
print(f'Senha User 2: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens.

# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user._Usuario__gera_usuario())  # Acesso, de forma ruim...
"""

# class lampada:
#
#     def __init__(self, cor, voltagem, luminosidade):
#         self.__cor = cor
#         self.__voltagem = voltagem
#         self.__luminosidade = luminosidade
#
# class ContaCorrente:
#
#     contador = 4999
#
#     def __init__(self, limite, saldo):
#         self.__numero = ContaCorrente.contador + 1
#         self.__limite = limite
#         self.__saldo = saldo
#         ContaCorrente.contador = self.__numero
#
# class Produto:
#
#     contador = 0
#
#     def __init__(self, nome, descricao, valor):
#         self.__id = Produto.contador + 1
#         self.__nome = nome
#         self.__descricao = descricao
#         self.__valor = valor
#         Produto.contador = self.__id
#
#     def desconto(self, porcentagem):
#         """Retorna o valor do produto com o desconto"""
#         return (self.__valor*(100 - porcentagem)) / 100
#
#
# from passlib.hash import pbkdf2_sha256 as cryp
#
# class Usuario:
#
#     def __init__(self, nome, sobrenome, email, senha):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__email = email
#         self.__senha = cryp.hash(senha, rounds = 200000, salt_size = 16)
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
#     def checa_senha(self, senha):
#         if cryp.verify(senha, self.__senha):
#             return True
#         return False
#
#     def __correr__(self, metros):
#         print(f"{self.nome} está correndo {metros} metros")
#
# p1 = Produto("Playstation 4", "Video Game", 2300)
# print(p1.desconto(50))
#
# user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")
# user2 = Usuario("Felicity", "Jone", "felicity@gmail.com", "654321")
#
# print(user1.nome_completo())
#
# print(user2.nome_completo())
#
# print(Usuario.nome_completo(user1)) # Estamos chamando o método a partir da classe. Porém, a classe
#                                     # não tem objeto. Então pasando a instância de um objeto para o método
#
# print(f"Senha: {user1._Usuario__senha}")
# print(f"Senha: {user1._Usuario__senha}")
#
# nome = input("Informe o nome: ")
# sobrenome = input("Informe o sobrenome: ")
# email = input("Informe o e-mail: ")
# senha = input("Informe a senha: ")
# confirma_senha = input("Confirme a senha: ")
#
# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
# else:
#     print("Senha não confere...")
#     exit(42)
#
# print("Usuário criado com sucesso!")
#
# senha = input("Informe a senha para acesso: ")
# if user.checa_senha(senha):
#     print("Acesso permitido")
# else:
#     print("Acesso negado")
#
# print(f"Senha User Criptografado: {user._Usuario__senha}")


# Métodos de classes

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0  # Para criar variáveis de classe apenas definimos a variável sozinha, ou seja, sem que
                  # estejam ligadas ao objeto através da palavra self presentes em métodos

    @classmethod  # Para criar um método de classe utilizamos o decorator @classmethod
    def conta_usuarios(cls): # O parâmetro cls em métodos de classe recebe a própria classe. Não é palavra chave, pode ser qualquer nome
        print(f"Temos {cls.contador} usuario(s) no sistema")

    @staticmethod  # Para criar um método estático, utilizamos o decorador @staticmethod
    def definicao():  # Nos métodos estáticos não temos ao objeto e nem à classe
        return 'UXR344'

    # Em pythons há os métodos de classe (que em outras linguagens são conhecidos como métodos estáticos) e
    # além disso também temos os métodos estáticos que são como os métodos de classe porém que não tem acesso
    # nem à classe nem ao objeto

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200000, salt_size = 16)
        Usuario.contador = self.__id
        print(f"Usuario criado: {self.__gera_usuario()}")


    def nome_completo(self):
        self.__qualquer = 0

        return f'{self.__nome} {self.__sobrenome}'


    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self): # Podemos criar métodos privados com o duplo underscore inicial
        return self.__email.split('@')[0]


    def __correr__(self, metros):
        print(f"{self.nome} está correndo {metros} metros")


# Método de Classe

user = Usuario("Felicity", "Jones", "felicity@email.com", "123456")
# print(user.__gera_usuario()) # Os métodos privados não podem ser acesssados diretamente pelo objeto
print(user._Usuario__gera_usuario()) # Podemos utilizar o nome feito através do Name Manling para acessar
                                     # o método privado (O acesso deve ser feito assim apenas em caso de muita necessidade)


# Quando criar méotos de classe e métodos de instância

# Nós metodos de classe não temos acesso ao objeto, pois não temos um lugar para entrar com o rótulo do objeto
# que geralmente é o self. Logo, criamos métodos de classe quando queremos apenas trabalhar com atributos de
# classe e nenhum atributo de instância.
# Criamos métodos de instância quando vamos utiizar pelo menos um atributo de instância.

#Métodos de classe são conhecidos como métodos estáticos em outras linguagens


#