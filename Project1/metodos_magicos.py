"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

Dunder > Double Underscore

# dunder repr -> Representação do objeto
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Quando nós temos os métodos __repr__ e __str__ implementados na mesma classe, o método
    # __str__ é o método que vai ser executado ao se utilizar o print. Não tem nada a ver com o método
    # resolution order. Método Resolution orde é para herança
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Um objeto do tipo livro foi deletado da memória")

    def __add__(self, outro):
        return f'{self.titulo} - {outro.titulo}'

    def __dir__(self):
        return ["Abc", "def"]

    def __rmul__(self, outro):
        if isinstance(outro, int):
            msg = ""
            for n in range(outro):
                msg += " " + str(self)
            return msg

        return "Não posso multiplicar"


livro1 = Livro("Python", "Geek University", 400)
livro2 = Livro("Inteligência Artificial", "Geek University", 350)


# print(livro1)
# print(livro2)
# print(len(livro1))
# print(len(livro2))

# del livro1
#
# del livro2

# print(livro1 + livro2)
# print(livro1 * 3)
print(3 * livro1)

# print(dir(livro1))
