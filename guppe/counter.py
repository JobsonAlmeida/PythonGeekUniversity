"""
Módulo Collections - Counter

Esse módulo collections é conhecido por high-performance container datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo collections counter que é parecido com um dicionário, contendo
como chave e elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento 

"""

# Utilizando o counter

from collections import Counter

#Podemos utilizar qualquer iteravel, estamos utilizando uma lista
lista = [1, 1, 2, 2, 3, 3 ,3, 1,1,2,3,4, 45, 45, 66 ]


res = Counter(lista)
print(type(res))
print(res)

print(Counter("Geek University"))

texto = """Mato Grosso foi um contratorpedeiro da classe Pará operado pela Marinha do Brasil de 1909 a 1946. Mato Grosso foi construído pela empresa naval britânica Yarrow Shipbuilders com o batimento de quilha ocorrendo em 1908, o lançamento ao mar em 23 de dezembro do mesmo ano e a comissão na armada em 24 de julho de 1909. Tinha um peso em deslocamento em carga total de 650 toneladas, media 70,24 metros de comprimento, boca de 7,16 metros, pontal de 4,27 metros e calado de 2,31 metros. Seus armamentos principais eram dois canhões de 101,6 milímetros e dois lançadores de torpedos de 457 milímetros. Alcançava a velocidade máxima de 27 nós (aproximadamente 50 quilômetros por hora)."""

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)
print(res.most_common(5))