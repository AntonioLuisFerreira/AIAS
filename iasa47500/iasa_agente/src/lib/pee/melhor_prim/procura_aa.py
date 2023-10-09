from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA

"""
    Classe ProcuraAA herda de ProcuraInformada

    Neste tipo de mecanismo de procura tem como objectivo encontrar o caminho mais curto entre dois estados.
    Para tal se suceder ele usa uma heuristica admissivel, consiste numa estimativa optimista dos custos que deveão ser sempre menores ou iguais ao custo minimo real.

    Como a heuristica o método de busca vai ser completo e optimo, por outras palavras se encontrar uma solucao deverá sempre ser uma a melhor solução possível, desde que os nós já visitados sejam guardados em memória.
    Para garantir estas caracteristicas sem ter a necessidade de guardar em memória, tem-se de ter uma heuristica cooesa.

    A aplicação de uma heurística coesa garante a optimização e a totalidade do algoritmo de busca,
    mesmo que os nós já visitados sejam eliminados.

"""
class ProcuraAA(ProcuraInformada):
    
    """
        O construtor da classe,
        chama o constructor da classe super
        e passa como paramêtro o AvaliadorAA.
    """
    def __init__(self):
        super().__init__(AvaliadorAA())