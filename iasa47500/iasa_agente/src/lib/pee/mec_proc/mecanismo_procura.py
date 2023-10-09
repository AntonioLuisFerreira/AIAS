from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
    A classe Mecanismo de Procura vai permitir procurar uma solução para um dado problema,
    utilizando o conceito de fronteira de exploração para memorizar e gerir nós explorados.

    No fundo é um mecanismo de exploração sucessiva de um espaço de estados.
"""

class MecanismoProcura(ABC):

    """
        Construtor da classe, recebe uma fronteira (array de nós não explorados),
        e armazena-os numa variável protegida.
    """
    def __init__(self, fronteira):
        self._fronteira = fronteira
        # Acrescentado
        # Inicialização das complexidades a 0
        self._complexidadeEspacial = 0
        self._complexidadeTemporal = 0
        ##

    # Acrescentado

    # Número máximo de nós mantidos em memória
    @property
    def complexidade_espacial(self):
        return self._complexidadeEspacial

    # Número de nós processados
    @property
    def complexidade_temporal(self):
        return self._complexidadeTemporal

    ##
    """
        O inicar memória consiste em iniciar a fronteira,
        de facto o que está a acontecer está-se iniciar um array de nós a vazio.
    """

    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        raise NotImplementedError

    """
        O método procurar recebe um problema para poder ser interpretado.
        Consiste em implementar um algoritmo geralista de resolução de problema.
        Vamos ter diferentes tipos de mecanismos de procura associados a diferentes tipos de fronteira (LIFO e/ou FIFO),
        e em alguns casos formas de memorizar nós explorados.

    """

    def procurar(self, problema):
        
        
        # iniciar a memoria
        self._iniciar_memoria()
        # criar um nó para o estado inicial
        no = No(problema.estado_inicial)
        # guardar o no em memoria
        #self._memorizar(no)
        self._fronteira.inserir(no)
        # enquanto não estiver
        while not (self._fronteira.vazia == True):
            # remove o nó da fronteira
            no = self._fronteira.remover()
            # se o estado do nó for o objectivo do problema retorna a solução
            if (problema.objectivo(no.estado)):
                return Solucao(no)
            # em caso de não ser vai passar para o próximo nó
            for no_sucessor in self._expandir(problema, no):
                # memorizar o nó seguinte
                self._memorizar(no_sucessor)

            # Acrescentado
            # Cada nó processado vai aumentar o contador de nos processados
            self._complexidadeTemporal = self.complexidade_temporal + 1
            ##

    """
        O método protegido expandir recebe um problema e um nó.
        Com o problema vai ver os operados e vai aplicar ao operador o estado nó, resulta num novo estado.
        Se existir um estado novo vai fazer uma exclusão ao nó com recurso ao yield.
    """

    def _expandir(self, problema, no):
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            # se existir um estado sucessor
            if estado_sucessor:
                # liberta o nó
                yield No(estado_sucessor, operador, no)
