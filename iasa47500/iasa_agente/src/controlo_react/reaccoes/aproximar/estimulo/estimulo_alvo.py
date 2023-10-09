from sae.ambiente.elemento import Elemento
from ecr.estimulo import Estimulo

"""
    A Classe EstimuloAlvo implementa a interface Estimulo,
    o estimulo tem como objectivo detetar um target em uma dada direção.
    


"""
class EstimuloAlvo(Estimulo):

    """
        O construtor da classe recebe uma direção e um gama, (a não ser passado valor default é de 0.9).

    """
    def __init__(self,direccao, gama = 0.9):
        self.__gama = gama
        self.__direccao = direccao

    """
        
        _ variavel anonima, não utilizada
        retorna uma intensidade
    """

    def detectar(self,percepcao):
        elem, dist, _ = percepcao.per_dir[self.__direccao]
        return self.__gama ** dist if elem == Elemento.ALVO else 0