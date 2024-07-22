"""
Estruturas lógias: and (e), or(ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

"""

ativo = False
logado = True

if not ativo and not logado:
    print("Bem vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

print(not True)

print("Checking is operator:")
if ativo is False:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")






