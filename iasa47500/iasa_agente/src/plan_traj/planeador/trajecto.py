
"""
    A classe Trajecto é representado por uma lista de nomes de localidades
"""
class Trajecto():
    """
        O construtor da classe recebe uma solução e descarecteriza a informação da solução,
        para que possa ser mais fácil para visualizar os resultados.
        Os parametros que são objectivos de ver na execução do executável,
        são as localidades a dimensão da solução e do custo final. 
    """
    def __init__(self,solucao):
        self.__localidades = [passo.estado.localidade for passo in solucao]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo

    """
        O que método mostrar faz é chamar as variaveis privadas guardadas no construtor e dar print dessas mesmas.
    """
    def mostrar(self):
        print('Solução: ', self.__localidades)
        print('Dimensao: ', self.__dimensao)
        print('Custo: ', self.__custo)
