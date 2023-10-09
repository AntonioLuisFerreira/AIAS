from pee.mec_proc.fronteira.avaliador import Avaliador

"""
    A classe AvaliadorCustoUniforma herda da Interface Avaliador onde tem de implmentar o método prioridade.
    Em causa está a utilização da função f(n) que diz a prioridade do nó será do tipo f(n) = estimativa do custo da solução através de n.
    
"""
class AvaliadorCustoUniforme(Avaliador):

    """
        O método prioridade neste caso,
        precisa de uma estimativa do custo da solução com recurso ao nó.
    """
    def prioridade(self,no):
        return no.custo