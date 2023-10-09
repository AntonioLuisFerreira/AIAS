from lib.mod.estado import Estado

class EstadoDeposito(Estado):
    """
        O construtor da classe guarda o parametro volume numa variavel privada, informação que caracteriza o estado
    """
    def __init__(self, volume):
        self.__volume = volume
        # o seu identificador só precisa ser calculado uma vez,
        #logo calcula-se o seu identificador no inicio e guarda-se numa variavel privada
        self.__id_valor = hash(self.__volume)

    # getter do volume
    @property
    def volume(self):
        return self.__volume

    """
        O método id valor vai retornar o valor calculado no construtor
    """
    def id_valor(self):
        return self.__id_valor