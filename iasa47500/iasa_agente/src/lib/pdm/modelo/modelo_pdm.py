from abc import ABC, abstractclassmethod
"""
    Representa a informação 
"""
class ModeloPDM(ABC):
    
    """
        Conjunto de estados do mundo
    """
    @abstractclassmethod
    def S(self):
        raise NotImplementedError
    
    """
        Conjunto de acções possíveis no estado s pertencente a S
    """
    @abstractclassmethod
    def A(self, s):
        raise NotImplementedError
    
    """
        Probabilidade de transição de s para s' através de a
    """
    @abstractclassmethod
    def T(self, s, a,sn):
        raise NotImplementedError
    
    
    """
        Retorno esperado na transição de s para sn através de a
    """
    @abstractclassmethod
    def R(self, s, a, sn):
        raise NotImplementedError
    
    """retorna um array"""
    @abstractclassmethod
    def Sucessores(self,s,a):
        raise NotImplementedError