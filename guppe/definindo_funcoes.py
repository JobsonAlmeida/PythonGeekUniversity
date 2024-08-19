"""
Definindo Funções

 - Funções são pequenos trechos de código que realizam tarefas específicas
 - Pode ou não receber uma entrada de dados e retornar uma saída de dados
 - Muito úteis para executar procedimentos similares por repetidas vezes

 Obs.: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação 
 para que a função seja simplificada

 Já utlizamos funções

 print()
 len()
 max()
 min()
 count()
 
"""

# Exemplo

cores = ['verde', 'amarelo', 'azul', 'branco']

#função integrada (built-in) do python
print(cores)

"""

 definindo funções 

 def nome_da_funcao(parametros_de_entrada):
    bloco_da_função

nome_da_funcao -> Sempre com letras minusculas e se for nome composto, separado por underline (Snake Case)
para definirmos uma função utilizamos a palavra reservada def
"""

def diz_oi():
    print("oi")

diz_oi()

def cantar_parabéns():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")

# cantar_parabéns()

# Podemos criar uma variável do tipo de uma função e executar esta função através da variável

canta = cantar_parabéns

canta()
