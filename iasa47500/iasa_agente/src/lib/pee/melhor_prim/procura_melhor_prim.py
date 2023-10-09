from abc import ABC, abstractclassmethod
from pee.mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade
from pee.mec_proc.procura_grafo import ProcuraGrafo

class ProcuraMelhorPrim(ProcuraGrafo):

    """
        O construtor da classe recebe como parametro um avaliador e guarda numa variavel protegida.
        É chamado o construtor da superclasse e em que passamos a fronteiraPrioridade
    """
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
    
    """
        O método protegido manter,
        Verifica se um nó recebido pode ou não ser mantido em memória,
        Existe duas condições para ser mantido:
        => em caso de não ter sido explorado, vai ser adicionado
        (realizado na verificação já é feita pelo manter() da superclasse).
        => em caso de já ter sido explorado mas o custo for menor a um nó do mesmo estado,
        vai ser substituido em explorados e adicionar numa posição mais prioritaria na fronteira.
        (Já realizado na classe FronteiraPrioridade)
    """
    def _manter(self,no):
        # chama o __It__() (less than) implementado na classe no
        # assim vai averiguar os custos dos nos
        return super()._manter(no) or no < self._explorados[no.estado]

    