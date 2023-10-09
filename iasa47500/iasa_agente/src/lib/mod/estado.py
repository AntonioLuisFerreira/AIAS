from abc import ABC, abstractclassmethod

"""
    Classe Estado define o problema e precisa de um identificador.
    É uma classe abstrata.
"""
class Estado(ABC):
    
    """
        O método id_valor retorna um inteiro,
        vai identificar o valor do identificador de estado.
    """
    @abstractclassmethod
    def id_valor(self):
        raise NotImplementedError
    
    # Os métodos seguintes são redefinições de métodos py para cumprir os requesitos do projecto.
    """
        O método __hash__ retorna o identificador do estado.
        Devido a ser um método hash value (representive intenger) ao
        usar-se encapsulamento retornado esse mesmo inteiro,
        não vai prejudicar o uso do método id_valor (método abstrato).
        Com a noção de identificador de estado será mudada dependendo do contexto de problema.
    """
    def __hash__(self):
        return self.id_valor()
    
    """
        O método __eq__ vai fazer "==" aos id's dos estados usando o representive intenger.
    """
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
