from abc import ABC, abstractmethod
"""
    A classe Problema representa um problema que irá ser solucionado pelo agente.

    No raciocínio automático tem uma capacidade de simular um mundo,
    existe um conceito de memória,
    existe um conceito de mundo,

    A nível de raciocínio automático, o problem poderá ser modelado em:
    => Estado, é um valor único que representa uma configuração ou situação no mundo;
    => Operador, é uma transformação ou transição entre estados,
    quando se aplica um operador a um estado gera-se um outro estado.
"""
class Problema(ABC):
    """
        Construtor da classe Problema,
        guarda os parametros em variáveis privadas
    """
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    """
        Propriedades de Apenas de Leitura,
        no py o @property só tem a capacidade de leitura (getter) e não de escrita (setter).

    """
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    @property
    def operadores(self):
        return self.__operadores
    
    """
        O objectivo é abstrato pois o objectivo,
        vai variando consoante o problema em causa.
    """
    @abstractmethod
    def objectivo(self, estado):
        raise NotImplementedError