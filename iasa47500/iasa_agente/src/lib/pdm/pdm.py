from pdm.mec_util import MecUtil
"""
    A classe PDM, é a classe principal da biblioteca de PDM(Processo de Decisão de Markov).
    É um processo que tem como função prever e controlar uma sequência de iterações,
    de algo com a noção de um prazo mais elevado.

    Vai ser necessário simular várias sequências de acções que poderam desencadear no futuro.
    
    Acções, Estados e Recompensas
    A cadeia de Markov será utilizada por métodos de uma classe que vai implementara interface ModeloPDM
    Esta classe fornece, assim, métodos que calculam a política (estratégia de seleção de acção, no caso não determinista).
"""
class PDM():
    """
        O construtor da classe:
            recebe um modelo que vai ser guardado numa variavel privada
            recebe gama e delta 
            com estes três parametros vão ser passadas para criar um objecto da classe MecUtil
    """
    def __init__(self,modelo,gama,delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)


    """
        O método público politica,
        É um método que vai retornar uma estratégia de seleção de acção,
        com base numa função de utilidade,
        no caso não deterministico
    """
    def politica(self, U):
        S = self.__modelo.S
        A = self.__modelo.A
        #inicializar a politica, é uma associação entre s e a
        pol = {}
        for s in S():
            #se existirem acções para o estado s
            if(A(s)):
                #vai se obter o maximo do conjunto de acordo com a função de avaliação de util_accao
                pol[s] = max(A(s), key=lambda a : self.__mec_util.util_accao(s,a,U))
        return pol

    """
        O método público resolver,
        Com base no PDM vai calcular a utilidade e politica.
        Returnando um tuple (Utilidade, Politica)
    """
    def resolver(self):
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol