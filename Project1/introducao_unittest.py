"""
Introdu��o ao m�dulo Unittest

Unittest -> Testes Unit�rios

O que s�o testes unit�rios?

Teste � a forma de se testar unidades individuais de c�digo fonte.

Unidades individuais podem ser: fun��es, m�todos, classes, m�dulos etc.

#OBS: Teste unit�rio n�o � espec�fico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de ent�o ganhamos todos os 'assertions' presentes no m�dulo.

Para rodar os testes, utilizamos unittest.main()


TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

M�todo                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x � verdadeiro
assertFalse(x)              x � falso
assertIs(a, b)              a � b
assertIsNot(a, b)           a n�o � b
assertIfNone(x)             x � None
assertIsNotNone(x)          x n�o � None
assertIn(a, b)              a est� em b
assertNotIn(a, b)           a n�o est� em b
assertIsInstance(a, b)      a � inst�ncia de b
assertNotIsInstance(a, b)   a n�o � inst�ncia de b


Por conven��o, todos os testes em um test case, devem ter seu nome
iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py


# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (e � recomendado) docstrings nos nossos testes.
"""

# Pr�tica - Utilizando a abordagem TDD

