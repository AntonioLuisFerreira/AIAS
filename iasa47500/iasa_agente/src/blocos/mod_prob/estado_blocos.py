from copy import deepcopy
from lib.mod.estado import Estado

class EstadoBlocos(Estado):
    
    def __init__(self, pilhas):
        self.__pilhas = pilhas
        self.__id_valor = hash(tuple( tuple(pilha) for pilha in self.__pilhas))

    
    @property
    def pilhas(self):
        return deepcopy(self.__pilhas)

    # @property
    # def pilhas(self):
    #     return self.__pilhas
    
    def id_valor(self):
        return self.__id_valor