from ecr.estimulo import Estimulo
"""
    A Classe Estimulo Obstaculo implementa a interface Estimulo,
    deteta obstaculo numa determinada direção

"""
class EstimuloObst(Estimulo):

    """
        Construtor da Classe EstimuloObst,
        Recebe uma direcao e armazena numa variável privada
        Recebe uma intensidade e armazena numa variável privada,
        se a variável não for instanciada o valor por default será 1.0 (float)
    """

    def __init__(self,direccao, intensidade = 1.0):
        self.__direccao    = direccao
        self.__intensidade = intensidade
    
    """
        O método detetar(), consiste em se existir contacto com o obstaculo,
        retorna a intensidade caso contrário retorna 0.
    """
    def detectar(self, percepcao):
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0
        