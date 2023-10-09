from abc import ABC, abstractmethod

"""
    A Interface Heuristiaca é maneira de resolver umproblema de forma rápida e eficiente.
    Vai ser usada por qualquer tipo de mecanismo de procura informada,
    vai calcular uma estimativa do custo entre dois nós,
    com base no conhecimento do problema por resolver.

    A interface em si dita que as classes que herdarem dela terão de implmentar o método h(n),
    sendo n o estado
"""
class Heuristica(ABC):

    """
        O método h(estado),
        vai devolver uma estimativa do custo de dado estado no trajetco
    """
    @abstractmethod
    def h(estado):
        """método abstrato"""