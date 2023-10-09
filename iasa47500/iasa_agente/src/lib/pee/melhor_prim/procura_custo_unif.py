from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUniforme

"""
    A classe ProcuraCustoUniforme herda de ProcuraMelhorPrim.
    Em mente a estratégia de controlo será a exploração dos primeiros caminhos com custo inferior.

    A função f(n) descrita na documentação da superclasse será com base,
    na estimativa do custo da solução através do nó n.
"""


class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
        O construtor da classe faz init da superclasse e passa o avaliador,
        no caso da procura de custo uniforme vai passar o Avaliador de custo uniforme,
        a prioridade do avaliador é ver o custo do nó.
    """

    def __init__(self):
        super().__init__(AvaliadorCustoUniforme())
