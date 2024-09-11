"""
Por que testar nosso c�digo?

Testes Automatizados!


         Aplica��o web
------------------------------------
|                                  |
|      frontend e backend          |
------------------------------------
|       testes automatizados       |
------------------------------------

Por que testar nosso c�digo?
    - Reduzir bugs (problemas) no c�digo existe;
    - Testes garantem que novos recursos da sua aplica��o n�o quebrem (alterem) recurso antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatora��o que costumamos fazer n�o tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD � utilizado est�gios de desenvolvimento:
    - Voc� escreve seu teste primeiro;
    - Ent�o voc� escreve o c�digo m�nimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Ent�o refatora o c�digo para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso � considerado completo;


Estes est�gios de desenvolvimento do TDD s�o quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;



"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} est� miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)

