"""
Raise

Levantando os próprios erros com raise

raise -> lança exceções

Obs.: O raise não é uma função é uma palavras reservada assim como def ou qualquer outra em python

Para simplificar pense no raise como sendo útil para que possamos criar nossas próprias excessões e mensagens de erro

A forma feral de utilização é

raise TipoDoErro("Mensagem de erro")

Obs.: O raise, assim como o return finaliza a função. Ou seja, nada após o raise é executado

"""

# raise ValueError("Valor Incorreto")

def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")

    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")

    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")

    print(f"O texto {texto} será impressoa na cor {cor}")

colore("Geek", "verda")