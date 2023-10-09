from pee.mec_proc.fronteira.fronteira import Fronteira
"""
    A fronteira fifo herda da classe fronteira
    FIFO quer dizer first in first out
"""
class FronteiraFIFO(Fronteira):

    """
        Como primeiro a entrar é o primeiro a sair lugar,
        tem de ser feito um append do nó no array privado de nos
    """
    def inserir(self, no):
        
        self._nos.append(no)