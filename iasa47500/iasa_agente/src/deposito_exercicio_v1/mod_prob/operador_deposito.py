from lib.mod.operador import Operador
from mod_prob.estado_deposito import EstadoDeposito

class OperadorDeposito(Operador):

    def __init__(self, volume_recepiente,custo):
        self.__custo = custo
        self.__volume_recepiente = EstadoDeposito(volume_recepiente)
    
    def aplicar(self,volume):
        return EstadoDeposito(volume + self.__volume_recepiente)
    
    def custo(self, estado, estado_suc):
        return self.__custo
    
        