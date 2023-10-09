from abc import ABC, abstractmethod

"""
    A classe Operador representa uma transição entre estados.
    Ao aplicar um operador a um estado gera-se um novo estado.
"""
class Operador(ABC):
    """
        O método abstrato aplicar o ser aplicado sobre um estado um operador vai criar um novo estado.
    """
    @abstractmethod
    def aplicar(self, estado):
        raise NotImplementedError

    """
        Dado um estado e o seu estado sucedor resulta o custo da operação.
    """
    @abstractmethod
    def custo(self, estado, estado_suc):
        raise NotImplementedError