"""
    A Classe Resposta, vai gerar a acção que o agente terá de realizar.

    A Resposta ao ser activada, recebendo a intensidade do ambiente,
    em consideração o recebido, vai gerar uma acção que o agente vai executar.

    Considerando o Diagrama UML:
        a Classe Resposta vai agregar uma acção (passado no construtor)
        Tem um método activar que recebe uma percepção e uma intensidade e retorna uma acção
"""

class Resposta:

    """
        O underscore antes do atributo vai declarar o atributo como protegido.
    """
    def __init__(self,accao):
        self._accao = accao
    
    """
        O método activar:
            define a prioridade da acação igual à intensidade da acção igual à intensidade
            dá return a acção associada à resposta
        O parametro percepção não é usado pois irá ser usado num futoro próximo.
        
        Recebe como intensidade de homissão 0.
    """
    def activar(self, percepcao, intensidade = 0.):
        self._accao.prioridade = intensidade
        return self._accao