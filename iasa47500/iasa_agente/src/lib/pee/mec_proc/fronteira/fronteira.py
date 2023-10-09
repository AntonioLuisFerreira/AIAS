from abc import ABC, abstractmethod

"""
    A classe Fronteira:
    A fronteira é uma resultante de nós não explorados.
    O mecanismo de procura termina a sua execução,
    quando tiver chegado ao objetivo,
    ou tiver explorado toda a sua fronteira.
"""
class Fronteira(ABC):

    # O construtor da classe consiste na inicialização da fronteira
    def __init__(self):
        self.iniciar()

    #vê se a fronteira esta vazia
    @property
    def vazia(self):
        if( len(self._nos) == 0):
            return True
        else:
            return False
        
    ##Acrescentado
    @property
    def dimensao(self):
        return len(self._nos)
    ##
    
    # O método iniciar que é chamado no construtor da classe consiste na criação de um array de nós vazio
    def iniciar(self):
        self._nos = []

    @abstractmethod
    def inserir(self,no):
        raise NotImplementedError

    # O método remover vai ao array nós e retira a primeira posição do array
    def remover(self):
        return self._nos.pop(0)
    
    