"""
Tipo string

"""


'uma string'
'234'
'a'
'42.3'

"uma string"
"234"
"a"
"True"
"42.3"

'''uma string'''
'''234'''
'''a'''

"""uma string"""
"""234"""
"""True"""


nome = 'Geek University'
print(nome)
print(type(nome))

nome = "'Gina's Bar"
print(nome)

nome = 'Angelina \' \nJolie'
print(nome)
print(type(nome))

nome = 'Geek Univsersity'
print(nome.upper())
print(nome.lower())

print(nome.split())

print(nome[0:5]) #slice de string

print(nome.split()[0])
print(nome[-1])
print(nome[::-1]) #Inversão da string

print("revertendo")
print(nome[0:5:-1]) #it doesn't work

print(nome.replace("G", "P"))
print(nome.replace("e", "i"))


