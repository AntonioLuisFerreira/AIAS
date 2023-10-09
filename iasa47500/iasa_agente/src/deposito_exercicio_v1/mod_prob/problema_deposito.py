from mod.problema.problema import Problema
from mod_prob.estado_deposito import EstadoDeposito
from mod_prob.operador_deposito import OperadorDeposito

class ProblemaDeposito(Problema):

    def __init__(self, ligacoes, vol_inicial, vol_final):
        super().__init__(EstadoDeposito(vol_inicial), [OperadorDeposito(ligacao.volume_introduzir,ligacao.custo) for ligacao in ligacoes])
        self.__volume_final = EstadoDeposito(vol_final)

    def objectivo(self, volume):
        return volume == self.__volume_final