from deposito_exercicio_professor.mod_prob.estado_deposito import EstadoDeposito
from deposito_exercicio_professor.mod_prob.operador_transferir import OperadorTansferir


class OperadorEncher(OperadorTansferir):
    """
        A implementação do aplicar é retornar o estado do novo volume,
        esse novo volume vai ser a soma do volume do estado passado como paramtro com volume guardado em memória.
    """
    def aplicar(self, estado):
        novo_volume = estado.volume + self._volume
        return EstadoDeposito(novo_volume)
    
    """__repr__ para dar o print"""
    def __repr__(self):
        return "Encher(%s)" % self._volume
