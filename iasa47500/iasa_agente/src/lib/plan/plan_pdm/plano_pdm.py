from plan.plano import Plano

"""
    A classe PlanoPDM herda de Plano,
        com a utilidade e a politica recebidas com parametros vai ser possível,
        determinar o a accao do estado.
        e mostrar a utilidade e a politica com recurso ao mostrar_valor da utilidade e a politica,
        desponibilizado na biblioteca SAE.
"""
class PlanoPDM(Plano):
    
    """
        O construtor da classe PlanoPDM,
        recebe como parâmetros a utilidade e a política,
        guardando-os em memória em variaveis privadas.
    """
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    """
        O método publico obter_accao:
        vai retornar o operador a aplicar face ao estado enviado,
        obtendo-o por indexação da Politica.
        Antes verifica se exsite politica.
    
    """
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
    """
        O método mostar vai chamar os métodos de amostragem implementados na classe Vista.
        Mostra cores em gradiente: verde se um estado, em contexto de utilidade, positivo e vermelho se negativo.
        Vai mostrar a política com setas amarelas.
    """
    def mostrar(self, vista):
        if self.__politica:
            vista.mostrar_valor(self.__utilidade)
            vista.mostrar_politica(self.__politica)