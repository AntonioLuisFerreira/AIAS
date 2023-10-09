from pee.melhor_prim.aval.heuristica import Heuristica
from math import dist

"""
    A classe HeurManhattan herda de heuristica
        Vai significar a métrica de distância ao objectivo, forma simplificada de chegar ao estado final.
        Para isso acontecer é necessário ter conhecimento do objectivo (estado final),
        o método h vai ditar a estimativa de custo dado estado 
"""
class HeurManhattan(Heuristica):

    """
        O construtor da classe vai receber o estado_final como parametro,
        e guardalo em memória numa variàvel privada
    """
    def __init__(self,estado_final):
        self.__estado_final = estado_final


    """
        O método h aplica a formula da distancia de Manhattan.
    """
    def h(self, estado):
        return abs(self.__estado_final.posicao[0] - estado.posicao[0]) + abs(self.__estado_final.posicao[1] - estado.posicao[1]) 