from lib.mod.estado import Estado

class EstadoDeposito(Estado):

    def __init__(self, volume):
        self.__volume = volume

    # getter da localidade
    @property
    def volume(self):
        return self.__volume

    def id_valor(self):
        return int(self.__volume)
    
    def __add__(self,estado):
        if estado.volume[0] == 'E':
            valor = int(estado.volume[-1])
        else:
            valor = -1.0 * int(estado.volume[-1])
        return self.__volume + valor