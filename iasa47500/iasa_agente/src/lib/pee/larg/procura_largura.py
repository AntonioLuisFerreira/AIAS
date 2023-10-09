from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO

"""
    A classe em questão herda de ProcuraGrafo
    A procura em largura,
    não avança para outro nível enquanto não pesquisa todos os nós do mesmo nível.
"""
class ProcuraLargura(ProcuraGrafo):
    """
        O construtor da classe faz super e como o Procuragrafo que por sua vez herda de Mecanismo de Procura recebe uma fronteira,
        para o caso da procura em largura passamos a fronteira fifo
    """
    def __init__(self):
       super().__init__(FronteiraFIFO())