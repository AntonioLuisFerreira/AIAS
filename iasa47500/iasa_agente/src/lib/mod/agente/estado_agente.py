from mod.estado import Estado

"""
    A classe EstadoAgente:
    Herda da classe Estado
    Vai representar uma posição que o agente pode tomar no mundo.
    Irá também agregar um tuplo com a informação das coordenadas x e y da posicao que o estado representa.
"""
class EstadoAgente(Estado):
    """
        O construtor da classe guarda a posicao numa variavel privada,
        clacula o id_valor com recurso ao método hash, 
        com o objectivo de ser menos pesado para a aplicação ser executada.
    """
    def __init__(self,posicao):
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao)

    #getter da posicao
    @property
    def posicao(self):
        return self.__posicao

    """
        O método id_valor retorna hash value já calculado no construtor e guardado em memória numa variável privada.
    """
    def id_valor(self):
        return self.__id_valor