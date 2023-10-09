from abc import ABC, abstractmethod

"""
    A interface ModeloPlan vai definir o representção do planeamento executado pelo agente,
    Estabelece o noção de ter métodos que informem o seu estado actual,
    bem como a lista de estados e operadores do domínio do problema.

    Vai ser utilizado na classe ModeloMundo
"""
class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """retorna o estado actual no dominio do modelo do mundo"""

    @abstractmethod
    def obter_estados(self):
        """retorna os estados no dominio do modelo do mundo"""

    @abstractmethod
    def obter_operadores(self):
        """retorna a lista de operadores no dominio do modelo do mundo"""
