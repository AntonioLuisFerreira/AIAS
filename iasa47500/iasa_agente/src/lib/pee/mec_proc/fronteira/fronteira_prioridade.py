from .fronteira import Fronteira
from heapq import heappush, heappop

"""
    A classe FronteiraPrioridade herda de Fronteira,logo é um tipo de prioridade.

    A inserção de nós na lista tem em conta a prioridade de cada nó. Sabendo que o mecanismo
    de procura por ordem utiliza uma função f para a avaliação de cada nó n gerado,
    a fronteira é ordenado por ordem crescente.
"""
class FronteiraPrioridade(Fronteira):

    """
        O construtor da classe,
        recebe como parametro um avaliador e guarda-o numa variavel protegida.
        e chama o construtor da superclasse
    """
    def __init__(self,avaliador):
        super().__init__()
        self._avaliador = avaliador
    
    """
        O método inserir com base da prioridade,
        recebe um no e vai fazer um heappush no array de nos,
        o tupolo (prioridade,no), para facilitar o mecanismo de inserção e remoção.
        
        Com recurso ao heappush o conteudo é ordenado de forma automatico de forma ascendente
    """
    def inserir(self,no):
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))
    

    """
        O método remover,
        faz a remoção do tuplo ou contrário do nó.

        O heappop remove sempre o índice 0 da lista,
        o nó com menor valor de f(n)
    """
    def remover(self):
        _ , no = heappop(self._nos)
        return no