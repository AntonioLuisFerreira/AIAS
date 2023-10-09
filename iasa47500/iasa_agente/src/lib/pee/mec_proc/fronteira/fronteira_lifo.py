from pee.mec_proc.fronteira.fronteira import Fronteira
"""
    A fronteira lifo herda da classe fronteira
    LIFO quer dizer last in first out
"""
class FronteiraLIFO(Fronteira):

    """
        Como último é em primeiro lugar, tem de ser feito um insert na posição de, 
        indice 0 o nó
    """
    def inserir(self, no):
        self._nos.insert(0,no)