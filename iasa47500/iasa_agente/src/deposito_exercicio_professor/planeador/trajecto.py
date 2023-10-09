
class Trajecto():
    """ 
        O construtor da classe recebe a solucao,
        trata as informações para dps mostrar os mesmos.
    
    """
    def __init__(self,solucao):
        self.__volumes = [passo.operador for passo in solucao if passo.operador != None]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo

    """
        O método mostrar faz os prints dos dados tratados no construtor da classe
    """
    def mostrar(self):
        print('Solução: ', self.__volumes)
        print('Dimensao: ', self.__dimensao)
        print('Custo: ', self.__custo)