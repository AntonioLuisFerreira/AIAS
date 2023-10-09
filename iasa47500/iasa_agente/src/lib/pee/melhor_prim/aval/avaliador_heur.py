from abc import ABC
from pee.mec_proc.fronteira.avaliador import Avaliador
"""
    A classe AvaliadorHeur herda da Interface Avaliador,
    vai definir a heuristica a ser usada.

    Herda também ABC pois as classes AvaliadorAA e AvaliadorSof vão herdar desta implementando o método prioridade().   
"""
class AvaliadorHeur(Avaliador,ABC):
    """
        O método definir_heuristica recebe como parametro uma heuristica e vai guarda-la numa variavel protegida
    """
    def definir_heuristica(self,heuristica):
        self._heuristica = heuristica