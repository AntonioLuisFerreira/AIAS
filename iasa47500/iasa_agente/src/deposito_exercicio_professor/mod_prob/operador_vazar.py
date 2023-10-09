from deposito_exercicio_professor.mod_prob.estado_deposito import EstadoDeposito
from deposito_exercicio_professor.mod_prob.operador_transferir import OperadorTansferir


class OperadorVazar(OperadorTansferir):
    
    """Implementação do aplicar,
    tem em consideração se o volume é menor que 0"""
    def aplicar(self, estado):
        novo_volume = estado.volume - self._volume
        if novo_volume < 0:
            novo_volume = 0
        return EstadoDeposito(novo_volume)
    
    """__repr__ para dar o print"""
    def __repr__(self):
        return "Vazar(%s)" % self._volume