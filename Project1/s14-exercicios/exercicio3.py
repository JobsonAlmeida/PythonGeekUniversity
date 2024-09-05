"""
3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca
"""

class Televisao:
    def __init__(self):
        self.__status = "desligada"
        self.__volume = 0
        self.__canal = 0

    def get_status(self):
        print(f"Status: {self.__status}")

    def get_volume(self):
        print(f"Volume: {self.__volume}")

    def get_canal(self):
        print(f"Canal: {self.__canal}")

    def ligar_desligar(self):
        self.__status = "ligada" if self.__status == "desligada" else "desligada"

    def volume_aumentar_diminuir(self, valor):

        if valor == "aumentar" and self.__volume < 100:
            self.__volume += 1

        elif valor == "diminuir" and self.__volume > 0:
            self.__volume -= 1

    def troca_canal(self, valor):

        if isinstance(valor, int):
            self.__canal = valor

        elif valor == "aumentar" and self.__volume < 100:
            self.__canal += 1

        elif valor == "diminuir" and self.__volume > 0:
            self.__canal -= 1

class ControleRemoto:
    def __init__(self, televisao):
        self.__televisao = televisao

    def get_status(self):
        self.__televisao.get_status()

    def get_volume(self):
        self.__televisao.get_volume()

    def get_canal(self):
        self.__televisao.get_canal()

    def ligar_desligar(self):
        self.__televisao.ligar_desligar()

    def volume_aumentar_diminuir(self, valor):
        self.__televisao.volume_aumentar_diminuir(valor)

    def troca_canal(self, valor):
        self.__televisao.troca_canal(valor)


televisao = Televisao()
controle = ControleRemoto(televisao)

controle.get_status()
controle.get_canal()
controle.get_volume()

controle.ligar_desligar()
controle.volume_aumentar_diminuir("aumentar")
controle.volume_aumentar_diminuir("diminuir")
controle.troca_canal("aumentar")
controle.troca_canal("aumentar")
controle.troca_canal("aumentar")

controle.get_status()
controle.get_canal()
controle.get_volume()


controle.ligar_desligar()
controle.troca_canal(10)


controle.get_status()
controle.get_canal()
controle.get_volume()



