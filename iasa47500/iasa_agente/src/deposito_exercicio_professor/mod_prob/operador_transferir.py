from abc import abstractmethod
from lib.mod.operador import Operador
from mod_prob.estado_deposito import EstadoDeposito

class OperadorTansferir(Operador):

    """
        O construtor da classe OperadorTransferir guarda o custo numa variavel protected.
    """
    def __init__(self, volume):
        self._volume = volume
        
    @abstractmethod
    def aplicar(self,volume):
       """ Aplicar a ser implementado consoante o tipo de operador"""
    
    """Método que calcula o custo tendo em conta aos estados do proprio com o estado sucessor"""
    def custo(self, estado, estado_suc):
        return abs(estado_suc.volume - estado.volume) ** 2
    

    
        