from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
""""
    A classe em questão herda de MecanismoProcura
    A Procura em Profundidade tem os mais recentes nos indices mais pequenos do array,
    consiste em explorar sempre pelos nós mais recentes memorizados.

"""
class ProcurarProfundidade(MecanismoProcura):
    """
        O construtor da classe faz super e como o MecanismoProcura recebe uma fronteira,
        para o caso da procura em profundidade passamos a fronteira lifo
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())
        
    """
        O método privado memorizar vai à fronteira criada no MecanismoProcura,
        e insere o nó
    """
    def _memorizar(self,no):
        self._fronteira.inserir(no)
        
        ##Acrescentado
        # Com recurso ao max permite comparar qual o tamanho das fronteiras do que já foi guardado na complexidadeEspacial
        # Esta abordagem foi feita com base na noção de que o tamanho do dicionario vai variando ao longo do tempo
        self._complexidadeEspacial = max(self._fronteira.dimensao, self.complexidade_espacial)
        