"""
Loop while


Forma geral

while expressão_booleana:
    //corpo do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão boolena é toda expressão onde o resultado é verdaeiro ou falso

num = 5
num < 5
"""

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs.: Em um loop while é importante que cuidemos do critério de parada para não causar loop infinito

#Exemplo 2

resposta = ''
while resposta != "sim":
    resposta = input("Já acabou Jéssica? ")


"""
C ou Java

while(expressão){
    intruções
}

do{


}
while(expressão)

No python não temos o loop do while

"""

