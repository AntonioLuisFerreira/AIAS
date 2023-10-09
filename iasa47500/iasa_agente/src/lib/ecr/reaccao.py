from .comportamento import Comportamento

"""
    A Classe Reaccao:
        é uma derivação da interface Comportamento,

    Com base no Diagrama UML:
        A Reaccao no seu contrutor recebe um estimulo e uma resposta
        Tem um método activar que recebe uma percepcção que retorna uma accao

"""
class Reaccao(Comportamento):

    """
        O construtor recebe um estimulo e uma resposta e armazena em variaveis privadas,
        para ser usado em métodos dentro da classe.
        O double underscore antes do atributo vai declarar o atributo como privado.
    """
    def __init__(self,estimulo,resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    

    """

        A intensidade é calculada com base na deteção de um estimulo
        O método activar só retorna se a intensidade for maoir que zero
        Return uma acção vai fazer a activação da resposta passada no seu construtor.
    """
    def activar(self,percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if(intensidade > 0):
            return self.__resposta.activar(percepcao,intensidade)
