from ecr.comportamento import Comportamento
from sae import Controlo

"""
    A classe ControloReact:
        É um controlo reativo do agente;
        Ele recebe um comportamento no seu construtor e guarda em memória numa variável privada
        O método processar de acordo com uma percepção retorna uma ação, ativação do comportamento.

"""
class ControloReact(Controlo):

    """
        No construtor de acordo com o diagrama UML guarda o comportamento em uma variável privada
        Double underscore representa um atributo privado, aplicando no caso expecifico ser o comportamento
    """
    def __init__(self,comportamento):
        self.__comportamento = comportamento

    """
        O método processar da classe Controlo Reactivo:
            consiste na activação do comportamento ao receber a percepcao detetada pelo agente no seu meio ambiente.
    """
    def processar(self,percepcao):
        return self.__comportamento.activar(percepcao)

