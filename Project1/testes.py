#!/usr/bin/python
# -*- coding: latin-1 -*-

import unittest

from atividades import comer, dormir, eh_engracada

"""
O arquivo de teste é um arquivo separadao. O arquivo de teste está no mesmo projeto que o arquivo que contém o 
código a ser testado, mas é um arquivo separado
"""

class AtividadesTestes(unittest.TestCase):
    # Essa funcao test_comer_saudavel é a função test. Esta função deve incluir uma unidade do nosso programa
    # que vai ser testada, que no nosso caso são as funções comer, dormir e eh_engracada.
    # Então temos a funcao test que engloba uma unidade do nosso código que vai ser testada.
    # O ideal é ter uma função test com para cada um dos diversos casos de teste para cada elemento unitário
    # a ser testado.
    # Por convenção, essa função deve ser chamar test_nomeDaFunçãoASerTestada. É importante que ela
    # comece com o nome test para o framework de teste uniitest conseguir identificá-las e executá-las
    # quando o arquivo de teste for executado

    def test_comer_saudavel(self):
        """Tentando o retorno com comida saudável"""
        self.assertEqual(
            comer("quiabo", True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida="pizza", eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        self.assertFalse(eh_engracada("Sergio Malandro"))
        self.assertTrue(eh_engracada("Jim Carrey"), "Deveria ser engraçado")

if __name__ == "__main__":
    unittest.main() # Esse main, varre o arquivo verifica todos as classes que são TestCase e executam um a um

