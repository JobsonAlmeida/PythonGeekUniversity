"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e 
imprima ela por extenso como “1 de janeiro de 20204”

"""

def converte_data(data):

    [dia, mes, ano] = data.split("/")

    #tratando do dia
    if(int(dia) < 10):
        dia = dia[1:2]
    
    #tratando o mês
    if(int(mes) == 1):
        mes = "janeiro"
    elif(int(mes) == 2):
        mes = "fevereiro"
    elif(int(mes) == 3):
        mes = "março"
    elif(int(mes) == 4):
        mes = "abril"
    elif(int(mes) == 5):
        mes = "maio"
    elif(int(mes) == 6):
        mes = "junho"
    elif(int(mes) == 7):
        mes = "julho"
    elif(int(mes) == 8):
        mes = "agosto"
    elif(int(mes) == 9):
        mes = "setembro"
    elif(int(mes) == 10):
        mes = "outubro"
    elif(int(mes) == 11):
        mes = "novembro"
    elif(int(mes) == 12):
        mes = "dezembro"
    else:
        mes = "desconhecido"
    
    return dia + " de " + mes + " de " + ano

print(converte_data("01/01/2024"))
print(converte_data("09/02/2025"))
print(converte_data("10/04/2026"))
print(converte_data("21/12/2030"))

