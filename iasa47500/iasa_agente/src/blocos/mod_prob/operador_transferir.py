from abc import abstractmethod
from lib.mod.operador import Operador


class OperadorTansferir(Operador):

    def __init__(self, numero_pilha):
        self._numero_pilha = numero_pilha
        
    @abstractmethod
    def aplicar(self,numero_pilha):
       """ Aplicar a ser implementado consoante o tipo de operador"""
    
    
    def custo(self, estado, estado_suc):
        return self._numero_pilha
    

    
        