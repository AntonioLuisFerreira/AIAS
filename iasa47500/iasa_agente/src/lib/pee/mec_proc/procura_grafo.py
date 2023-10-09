from pee.mec_proc.mecanismo_procura import MecanismoProcura
from abc import ABC
"""
    A classe procura grafo, herda de MecanismoProcura, representa um mecanismo de procura em garfo,
    a procura em garfo permite manter a indormção de nós já explorados (memória).
    Com dados guardados em memória permite com que o sistema se torne mais eficiente,
    pois ao contrário de mecanismo de procura em profundidade é mais resistente à possibilidade de ocorrer loops.

    Para fazer a parte da memória é agregado um dicionário, com a sua constituição a informação,
    relatica ao estados dos nós explorados.
"""
class ProcuraGrafo(MecanismoProcura,ABC):

    """
        Método protegido iniciar memória como o nome sugere é responsável,
        por inicar a memória com recurso ao super() da classe MecanismoProcura,
        dar start ao dicionário de explorados a vazio, o dicionário também é protegido.
    """
    def _iniciar_memoria(self):
        # dá overwrite à classe mãe
        super()._iniciar_memoria()
        self._explorados = {}

    """
        O métofo protegido manter recebe um nó retorna um boolean com a informação se o nó em causa já pertence ao dicionário.
    """
    def _manter(self,no):
        return no.estado not in self._explorados
    """
        O método protegido memorizar recebe um nó como parametro,
        vê se é para manter(usando o método _manter),
        se sim vai ao dicionario buscar o nó e insere o nó na fronteira.
        "Recordando que a fronteira é um array de nós não explorados".
    """
    def _memorizar(self,no):
        
        if (self._manter(no)):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
            
            ## Acrescentado
            # Com recurso ao max permite comparar qual o tamanho dos explorados do que já foi guardado na complexidadeEspacial
            # Esta abordagem foi feita com base na noção de que o tamanho do dicionario vai variando ao longo do tempo
            self._complexidadeEspacial = max(len(self._explorados), self._complexidadeEspacial)
            ##

    
