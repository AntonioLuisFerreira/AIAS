from mod.problema.problema import Problema

"""
    A classe ProblemaPlan herda de Problema,
        neste contexto o planeamento do trajecto fai ser feito com base na melhor proposta.
        mecanismo de melhor primeiro.
"""
class ProblemaPlan(Problema):

    """
        O construtor da classe recebe um modelo e o estado final,
            vai chamar o construtor da superclasse enviando o estado inicial e os operadores do problema,
            vai guardar em memória o estado final para posteriormente poder verificar se é objectivo
    """
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(),modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    """ 
        O método objectivo recebe um estado,
            tem como função comparar se o estado recevido é igual ao estado final
            retorna true ou false
    """
    def objectivo(self,estado):
        return estado == self.__estado_final