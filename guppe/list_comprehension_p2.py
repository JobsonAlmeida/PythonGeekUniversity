"""
List Comprehension (Compreensão de Lista)

- Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe

'variavel_lista' = [dado_processado for dado in iteravel ]
Eu quero criar uma lista com varios 'dado_processado' para cada 'dado' presente em 'iteravel'. A lista gerada
atribuída para 'variavel_lista' 

#parte 2

Nós podemos adicionar estruturas condicionais lógicas às nossas list comprehensions

'variavel_lista' = [dado_processado for dado in iteravel if condicao_para_cada_dado ]
Eu quero criar uma lista com varios 'dado_processado' para cada 'dado' presente em 'iteravel' se o dados respeitar
a condição 'condicao_para_cada_dado'. A lista gerada atribuída para 'variavel_lista' 

"""


numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if numero %2 == 0]
impares = [numero for numero in numeros if numero %2 != 0]

print(pares)
print(impares)

pares = [numero for numero in numeros if (not numero%2)]
imapares = [numero for numero in numeros if numero%2]

print(pares)
print(impares)

# 2

#Podemos colocar if else na área de condição para cada dado
# Forma  geral
# [dado_processado_do_if if avalicao1 else dado_processado_do_else for dado in iteravel if condicao_para_cada_dado ]

res = [numero*2 if numero %2 == 0 else numero/2 for numero in numeros]
print(res)



