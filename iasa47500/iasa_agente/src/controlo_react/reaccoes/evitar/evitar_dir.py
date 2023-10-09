from controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

"""
    A Classe Evitar Direção herda de Reaccao,
    O comportamento quando deteta um obstáculo em determinada direção
"""
class EvitarDir(Reaccao):
    
    """
        O construtor da classe EvitarDir chama o método super da classe Reaccao,
        logo tem de receber como parametros um estimulo e uma resposta

    """
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)