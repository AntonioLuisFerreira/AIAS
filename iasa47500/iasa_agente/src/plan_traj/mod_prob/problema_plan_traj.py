from mod.problema.problema import Problema
from mod_prob.estado_localidade import EstadoLocalidade
from mod_prob.operador_ligacao import OperadorLigacao

"""
    A classe ProblemaPlanTraj herda da classe problema.
    Neste caso o problema de partir de uma localização inicial para uma final,
    com isto é pretendido obter o plano do trajecto a ser realizado para chegar ao destino.
"""
class ProblemaPlanTraj(Problema):

    """
        O construtor da classe  recebe como parametros ligações, lista de ligaçoes que consiste numa lista da classe OperadorLigacao,

        Chama o construtor da superclasse enviando um estadoLocalidade correspondente do estado incial, a lista de Operador de Ligações.
        Para além vai guardar como atributo final outro EstadoLocaludade, correspondente ao estado final
    """
    def __init__(self, ligacoes, loc_inicial, loc_final):
        super().__init__(EstadoLocalidade(loc_inicial), [OperadorLigacao(ligacao.origem,ligacao.destino, ligacao.custo) for ligacao in ligacoes])
        self.__estado_final = EstadoLocalidade(loc_final)

    """
        O método publico objectivo tem como função ver se o estado passado corresponde ao estado final guardado no construtor da classe
    """
    def objectivo(self, estado):
        return estado == self.__estado_final