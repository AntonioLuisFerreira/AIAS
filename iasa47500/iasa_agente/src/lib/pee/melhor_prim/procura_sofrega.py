from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.aval.avaliador_sof import AvaliadorSofrega

"""
    A Classe ProcuraSofrega herda de ProcuraInformada

    Este algoritmo de busca selecionada iterativa vai optar pelo caminho que parecer ser melhor possível (no momento).
    Vai construindo a solução passo a passo.
    Ele é completo, sempre que encontrar uma solução podendo ele ser optima ou não,
    pois o algoritmo não considera adquedamente os constrangimentps ao longo do processamento.

    Ele é também heuristico, utiliza apenas uma função heuristica para resolver o problema.
    Para este caso em especifico ele usa o avaliador AvaliadorSofrega como parte da sua implementação na classe ProcuraInformada.
"""
class ProcuraSofrega(ProcuraInformada):
     
    """
        O construtor da classe,
        chama o constructor da classe super
        e passa como paramêtro o AvaliadorSofrega.
    """
    def __init__(self):
        super().__init__(AvaliadorSofrega())