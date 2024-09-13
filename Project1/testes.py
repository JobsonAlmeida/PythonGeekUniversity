#!/usr/bin/python
# -*- coding: latin-1 -*-

import unittest

from atividades import comer, dormir, eh_engracada

"""
O arquivo de teste � um arquivo separadao. O arquivo de teste est� no mesmo projeto que o arquivo que cont�m o 
c�digo a ser testado, mas � um arquivo separado
"""

class AtividadesTestes(unittest.TestCase):
    # Essa funcao test_comer_saudavel � a fun��o test. Esta fun��o deve incluir uma unidade do nosso programa
    # que vai ser testada, que no nosso caso s�o as fun��es comer, dormir e eh_engracada.
    # Ent�o temos a funcao test que engloba uma unidade do nosso c�digo que vai ser testada.
    # O ideal � ter uma fun��o test com para cada um dos diversos casos de teste para cada elemento unit�rio
    # a ser testado.
    # Por conven��o, essa fun��o deve ser chamar test_nomeDaFun��oASerTestada. � importante que ela
    # comece com o nome test para o framework de teste uniitest conseguir identific�-las e execut�-las
    # quando o arquivo de teste for executado

    def test_comer_saudavel(self):
        """Tentando o retorno com comida saud�vel"""
        self.assertEqual(
            comer("quiabo", True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida="pizza", eh_saudavel=False),
            'Estou comendo pizza porque a gente s� vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado ap�s dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        self.assertFalse(eh_engracada("Sergio Malandro"))
        self.assertTrue(eh_engracada("Jim Carrey"), "Deveria ser engra�ado")

if __name__ == "__main__":
    unittest.main() # Esse main, varre o arquivo verifica todos as classes que s�o TestCase e executam um a um

