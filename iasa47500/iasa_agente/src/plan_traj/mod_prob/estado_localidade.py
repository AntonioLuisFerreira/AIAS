from lib.mod.estado import Estado

"""
    A classe EstadoLocalidade herda de estado, logo vai implmentar o método abstrato da mesma, id_valor,
    onde vai retornar a indentificação do estado.

    No contexto do Problema representa uma localidade no trajecto.
"""
class EstadoLocalidade(Estado):
    
    """
        O construtor da classe guarda a localidade num atributo privado
    """
    def __init__(self, localidade):
        self.__localidade = localidade

    # getter da localidade
    @property
    def localidade(self):
        return self.__localidade

    """
        O método id_valor retorna o identificador da localidade.
    """
    def id_valor(self):
        return int(self.__localidade[-1])
        # return ord(self.__localidade[-1]) - ord('0')
        