from abc import ABC, abstractmethod
from .comportamento import Comportamento

"""
    A Classe ComportComp:
        Deriva da classe Comportamento, logo tem de ser implementado o métdo activar
        A principal diferença face a um comportamento simples consiste em um comportamento
        composto constituir por mais do que um comportamento
        Em uma lista de objectos do tipo comportamento.
"""
class ComportComp(Comportamento, ABC):

    """
        O contrutor da classe:
            de acordo com o diagrama UML recebe uma lista de comportamentos privada
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    """
        O método activar respeita a interface implementada pelo Comportamento.
        O Comportamento Composto, vai se ativando consistemente os seus próprios comportamentos,
        obtendo  ações resultantes.
        Por fim, é escolhida uma única ação a ser executada.
    """
    def activar(self, percepcao):
        # inicialização do array de accoes
        accoes = []

        for i in self.__comportamentos:
            accao = i.activar(percepcao)
            #verificacao se accao não é null
            if(accao):
                accoes.append(accao)
        #verificacao se a lista está vazia
        if(accoes):
            return self.selecionar_accao(accoes)

    @abstractmethod
    def selecionar_accao(self, accoes):
        """
            Método vai permitir selecionar uma ação com base no mecanismo de reação
            escolhido em base da hierarquia ou da prioridade do projecto.
        """