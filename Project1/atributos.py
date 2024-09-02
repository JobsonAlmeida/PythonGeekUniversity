"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;


# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.


# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedrir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AttributeError


print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do contrutor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

"""

# Classes com Atributo de Instância Público


# class Lampada:
#
#     def __init__(self, voltagem, cor):
#         self.voltagem = voltagem
#         self.cor = cor
#         self.ligada = False
#
#
# class ContaCorrente:
#
#     def __init__(self, numero, limite, saldo):
#         self.numero = numero
#         self.limite = limite
#         self.saldo = saldo
#
#
# class Produto:
#
#     def __init__(self, nome, descricao, valor):
#         self.nome = nome
#         self.descricao = descricao
#         self.valor = valor
#
#
# class Usuario:
#
#     def __init__(self, nome, email, senha):
#         self.nome = nome
#         self.email = email
#         self.senha = senha
#
#
# # Atributos Públicos e Atributos Privados
#
# class Acesso:
#
#     def __init__(self, email, senha):
#         self.email = email
#         self.__senha = senha
#
#     def mostra_senha(self):
#         print(self.__senha)
#
#     def mostra_email(self):
#         print(self.email)
#
#
# # Refatorar a classe Produto
#
# class Produto:
#
#     # Atributo de classe
#     imposto = 1.05  # 0.05% de imposto
#     contador = 0
#
#     def __init__(self, nome, descricao, valor):
#         self.id = Produto.contador + 1
#         self.nome = nome
#         self.descricao = descricao
#         self.valor = (valor * Produto.imposto)
#         Produto.contador = self.id
#
#
# # Atributos Dinâmicos -> Um atributos de instância que pode ser criado em tempo de execução.
#
# # OBS: O atributo dinâmico será exclusivo da instância que o criou.
#
# p1 = Produto('PlayStation 4', 'Video Game', 2300)
#
# p2 = Produto('Arroz', 'Mercearia', 5.99)
#
# # Criando um atributo dinâmico em tempo de execução
#
# p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso
#
# print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
#
# # print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')
#
# # Deletando atributos
#
# print(p1.__dict__)
# print(p2.__dict__)
#
# # print(Produto.__dict__)
#
# del p2.peso
# del p2.valor
# del p2.descricao
#
# print(p1.__dict__)
# print(p2.__dict__)

# Atributos de instâncias

""" em java

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}
"""

class Lampada:
    def __init__(self, voltagem, cor): # Em python, o método contrutor tem o nome de __init__ e não o mesmo nome da classe
        self.voltagem = voltagem # O duplo underline indica o private de variáveis em Python
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo= saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Teste:
    def __init__(cerveja, nome, idade): # O primeiro parâmetro de um método recebe um rótulo para o próprio obeto
        cerveja.nome = nome             # Esse rótulo pode ser qualquer nome. Por convenção colocamos a
        cerveja.idade = idade           # palavra self, mas pode ser qualquer nome. Veja então que self  não
        self = 10                       # é uma palavra reservada


# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

# Atributos públicos e atributos privados


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Acesso("user@gmail.com", "123456")

print(user.email)
print(user._Acesso__senha)
user.mostra_senha()

#

user1 = Acesso("joao@gmail.com", 123456)
user2 = Acesso("pedro@gmail.com", 4521475)

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

p1 = Produto("Plastation 4", "video game", 2300)
p2 = Produto("Xbox S", "Video Game", 4500)

# Atributos de instância -> tem seus valores de acordo com a instância criada

# Atrivutos de classes -> são atributos que são declarados diretamente na classe, ou seja fora do construtor.
# Geralmente já inicializamos um valor e este valor é compartilahdo entre todas as instâncias da classe.
# Ou seja, ao invés de cada instância da classe ter seus próprios
# # valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# # terão o mesmo valor para este atributo.


class Produto:

    #Atributo de classe
    imposto  = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id # Parâmetros de classe são acessos através do nome da classe

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;


p1 = Produto("Playstation 4", "Video Game", 2300)
p2 = Produto("Xbox S", "Vídeo Game", 4500)

print(p1.imposto)
print(p2.imposto)
print(p1.valor)
print(p2.valor)
print(Produto.imposto)
print(p1.id)
print(p2.id)

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução
# O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto("Playstation 4", "Video Game", 2300)
p2 = Produto("Arroz", "Mercearia", 5.99)

p2.peso = "5kg" #Note que na classe Produto não existe o atributo peso

print(f"{p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")
# print(f"{p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}") # o objeto p1 não possui o atributo peso. logo será lançado um erro

# Assim como é possível adictionar atributos dinamicamente é possível deletar atributos dinamicamente

print(p1.__dict__) # O método dict devolve um dicionário com os atributos de instância do objeto
print(p2.__dict__)

del p2.peso # deletando a referência p2

print(p1.__dict__) # O método dict devolve um dicionário com os atributos de instância do objeto
print(p2.__dict__)

del p2.valor # deletando a referência p2. Podemos deletar qualquer atributo da instância

print(p1.__dict__) # O método dict devolve um dicionário com os atributos de instância do objeto
print(p2.__dict__)

