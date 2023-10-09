from plan.plano import Plano

"""
    A classe PlanoPee herda de Plano,
        com a solução recebida com parametro vai ser possível,
        determinar o operador do estado com recurso aos métodos definidos na classe Solução.
        e mostrar a solução com recurso ao mostrar_solução desponibilizado na biblioteca SAE.
"""
class PlanoPEE(Plano):
    
    """
        O construtor da classe recebe como parametro uma solução
        e guarda-la em memória numa variavel privada.
    """
    def __init__(self,solucao):
        self.__solucao = solucao

    """
        O método obter_accao recebe um estado,
            primeiro verifica se a solução é do tipo None, caso negativo
            procede para remover o primeiro no da solução,
            verfica se o no retirado tem o mesmo estado que estado recebido como parametro,
            caso afirmativo o método irá retorna o operador do primeiro no da solução.
    """
    def obter_accao(self,estado):
        
        if self.__solucao != None:
            no = self.__solucao.remover()
            no_seguinte = self.__solucao[0]
            if no.estado == estado:
                return no_seguinte.operador
    
    """
        O método mostrar vai chamar o método de amostragem da solução implementado na classe Vista.
    """
    def mostrar(self, vista):
        vista.mostrar_solucao(self.__solucao)