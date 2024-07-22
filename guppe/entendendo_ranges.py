"""
Ranges

- Precisamos conhecer o looop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor o loop for

Ranges são utilizados para gerar sequencias numericas não de forma aleatória mas de maneira especificada

Formas gerais

range(valor de parada)
Obs.: Valor de parada não inclusive (início padrão 0 e passo de 1 em 1)


"""

#Forma 1
#range(valor de parada)
#Obs.: Valor de parada não inclusive (início padrão 0 e passo de 1 em 1)
for num in range(11):
    print(num)

#Forma 2
#range(valor_de_inicio, valor_de_parada)
#Obs.: Valor de parada não inclusive (início padrão 0 e passo de 1 em 1)

for num in range(4, 11):
    print(num)

#Forma 3
#range(valor_de_inicio, valor_de_parada, passo)
for num in range(5, 51, 5):
    print(num)


print("---- Forma 4 -----")
#Forma 4
#range(valor_inicio, valor_de_parada, passo negativo)

for num in range(50, 5, -5):
    print(num)

