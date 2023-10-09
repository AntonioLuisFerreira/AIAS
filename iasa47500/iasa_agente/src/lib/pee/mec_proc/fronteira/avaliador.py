from abc import ABC, abstractclassmethod

"""
    Interface Avaliador, tem como proposito definir a avaliação de prioridade de nós.
    Define o método prioridade que retorna a prioridade de um nó em causa.
"""
class Avaliador(ABC):
    """
        O valor de f(n) é representante da sua prioridade
    """
    @abstractclassmethod
    def prioridade(self,no):
        raise NotImplementedError