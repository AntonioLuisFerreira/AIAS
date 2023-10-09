from pee.melhor_prim.aval.heuristica import Heuristica
from math import dist

"""
    A classe HeurDist herda de heuristica
        Vai significar a métrica de distância ao objectivo, forma simplificada de chegar ao estado final.
        Para isso acontecer é necessário ter conhecimento do objectivo (estado final),
        o método h vai ditar a estimativa de custo dado estado 
"""
class HeurDist(Heuristica):

    """
        O construtor da classe vai receber o estado_final como parametro,
        e guardalo em memória numa variàvel privada
    """
    def __init__(self,estado_final):
        self.__estado_final = estado_final

    """
        O método h tem como objectivo devolver uma estimativa do custo de um dado estado no trajecto.
        Para este caso a avaliação é feita por base na distância até ao estado final
    """
    def h(self, estado):
        return dist(self.__estado_final.posicao, estado.posicao)