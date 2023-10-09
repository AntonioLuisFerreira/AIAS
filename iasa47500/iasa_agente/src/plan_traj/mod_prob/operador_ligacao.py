from lib.mod.operador import Operador
from mod_prob.estado_localidade import EstadoLocalidade

"""
    A classe OperadorLigacao herda de Operador logo vai implementar os metodos abstratos da classe Operador.
    Ao realizar a classe Operador de forma a que a arquitetura do cenário em teste possa set efetuada.
    Vai representar a transição entre duas localidades do cenário em teste, tendo associado a informação do custo.
"""
class OperadorLigacao(Operador):
    
    """
        O construtor da classe guarda o custo recebido como atributo,
        cria objectos da classe EstadoLocalidade passando a origem e destino,
        (str que significão o nome da localidade deste operdaor)
    """
    def __init__(self, origem,destino,custo):
        self.__custo = custo
        self.__estado_origem  = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)

    """
        O método publico aplicar concretiza o método da interface Operador,
        Tem como objectivo de verificar se o esrado enviado é o mesmo ao estado de origem,
        se sim o método retorna o estado de destino.
    """
    def aplicar(self, estado):
        if(estado == self.__estado_origem):
            return self.__estado_destino
        
    """

        O método publico custo concretiza o método da interface Operador,
        Para além dos parametros que o método recebe para esta implementação, 
        independentemente dos estados o custo é fixo
    """
    def custo(self, estado, estado_suc):
        return self.__custo