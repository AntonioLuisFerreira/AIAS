from abc import ABC, abstractclassmethod

"""
    A interface Comportamento:
        
        Com base na arquitetura de agentes reativos,
        importa a modularidade e o encapsulamento de modo
        a diminuir a complexidade.

    Pretende-se definir um conceito de módulo comportamental,
    que vai agregar as várias reações.
"""
class Comportamento(ABC):

    """
        Como Comportamento é uma interface não tem construtor,
        mas os métodos somarizados na interface tem de receber como parametro,
        self devido à documentação do Python.
    """


    @abstractclassmethod
    def activar(self,percepcao):
        """
            Ativar um comportamento
        """