from abc import ABC, abstractmethod
"""
    Interface Planeador,
        Vai definir a noção que um planeador terá de ter um método planear que irá receber um modelo do mundo e objectivos.
"""
class Planeador(ABC):
    
    @abstractmethod
    def planear(self,modelo_plan,objectivos):
        """vai planear"""