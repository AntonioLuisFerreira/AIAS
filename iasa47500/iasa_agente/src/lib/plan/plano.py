from abc import ABC, abstractmethod

"""
    A interface Plano vai defenir a noção de opter acção e de mostrar.
"""
class Plano(ABC):

    @abstractmethod
    def obter_accao(self,estado):
        """retorna um operador com uma acção"""


    @abstractmethod
    def mostrar(self,vista):
        """mostra a vista na janela pygame com recurso aos métodos da classe Visualização"""