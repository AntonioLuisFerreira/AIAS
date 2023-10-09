from ecr.hierarquia import Hierarquia

from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar

"""
    A Classe Recolher herda de comportamento composto
    onde é instanciado os três comportamentos AproximarAlvo(), EvitarObst(), Explorar()

"""
class Recolher(Hierarquia):
    """
        No método super da classe Comportamento Composto recebe um array com Comportamentos,
        necessários para o comportamento pretendido que o agente tenha
    """
    def __init__(self):
        super().__init__([AproximarAlvo(),EvitarObst(),Explorar()])