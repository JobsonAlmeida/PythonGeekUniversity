""" 
Módulo Colletion - Default Dict

Ao criar um dicionário utilizando o Default Dict, nós informamos um valor default podendo utilizar um lambda para isso. 
Este valor será utlizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe,  essa chave será 
criada e o valor default será atribuído.  


"""

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)

print(dicionario['curso'])

# print(dicionario['adb']) # Quando a chave não existe, um erro KeyError é lançado

print(dicionario.get('curso'))

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)  
dicionario['curso'] = "Programação em Python"
print(dicionario)
dicionario['outro'] # KeyError no dicionário comum, mas aqui não
print(dicionario)
dicionario['outro2'] # KeyError no dicionário comum, mas aqui não
print(dicionario)


