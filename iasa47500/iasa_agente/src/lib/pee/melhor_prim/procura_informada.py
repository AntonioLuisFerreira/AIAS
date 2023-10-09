from abc import ABC
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
    A classe ProcuraInformada herda de ProcuraMelhorPrim,
    
    A procura informada vai tirar partido da heuristica para obter uma estimativa do custo entre dois nós.
"""
class ProcuraInformada(ProcuraMelhorPrim):
    """
        O método procurar recebe um problema e um heuristica,
        guarda a heuristica numa variavel protegida,
        define o avaliador com a heuristica recebida como parametro
        e retorna o procurar da classe super passando o problema como parametro
    """
    def procurar(self,problema, heuristica):
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)