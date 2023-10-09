from pdm.pdm import PDM
from plan.planeador import Planeador
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM


"""
    A classe PlaneadorPDM herda de Planeador.
    Tem como objetivo realizar a resolução de um problema - planeamento do movimento do agente a fim de atingir certos
    objetivos, por meio do Processo de Decisão de Markov.

    Tem de concretizar os métodos que permitem executar essa função, tomando ainda
    partido da classe ModeloPDMPlan , da classe PDM e da classe PlanoPDm.
"""
class PlaneadorPDM(Planeador):

    """
        O construtor da classe PlaneadorPDM recebe o gama e o delta_max
        se não forem passados nada os valores default são 0.85 e 1 respetivamente,
        guardando-os em variaveis privadas.
    """
    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max


    """
        O método planear recebe um modelo de plano e uma lista de objetivos.
        Tem como objectivo ativar o resolver do mecanismo de procura em uso, guardando a utilidade e a politica.
        returnado uma instancia do objecto PlandoPDM passando como parametros a utilidade e a politica.

        Para usar o resolver do pdm primeiro tem criar um modelo_pdm_plan com recurso ao modelo_plan e os objectivos.
        O pdm para ser criado recebe como parametros modelo_plan, gama e o delta_max.
    """
    def planear(self,modelo_plan, objectivos):
        modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo_pdm_plan, self.__gama, self.__delta_max)
        utilidade, poltica = pdm.resolver()
        return PlanoPDM(utilidade, poltica)