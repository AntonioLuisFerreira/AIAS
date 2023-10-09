from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

"""
    A classe ModeloPDMPlan é uma classe de modulação do mundo para ser usada,
    na resolução de um problema pelo processo de Markov.

    Vai herdar de ModeloPlan e de ModeloPDM, 
    A classe serve de interpulação para o modelo_plan enviando ao construtor, que já tem um conjunto de funções.

    A junções destes dois contrato vai possibilitar o código já realizado compativel com Markov.
"""
class ModeloPDMPlan(ModeloPlan,ModeloPDM):

    """
        O construtor da classe vai guardar em memória os três parametros,
        sendo eles o modelo_plan, rmax, e os objectivos.
        A recompensa máxima(rmax) que o agente pode atingir, valor default é 1000.
        També no constutor se vai calcular as transições possíveis.
        O dicionário transicoes é constituido por estado atual, acção e estado sucessor.
        O estado sucessor é calculado apartir da aplicção da acção ao estado atual.

    """
    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__rmax = rmax
        self.__objectivos = objectivos
                        
        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                #Modelo determinista
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s,a)] = sn

    """
        Retorna o estado atual do modelo do mundo.
    """
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    """
        Retorna uma lista de estados do modelo do mundo.
    """
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    """
        Retorna uma lista de operadores do modelo do mundo.
    """
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    """
        O método publico S vai devolver um conjunto de estados presentes no contexto do mundo.
        Na realidade tem a mesma funcionalidade que o método obter_estados, 
        mas devido à necessidade da implementação das interfaces, vamos somente chamar o método
    """
    def S(self):
        return self.obter_estados()

    """
        O método publico A vai devolver um conjunto de operações num dados estado.
        Na realidade tem a mesma funcionalidade que o método obter_operadores, 
        mas devido à necessidade da implementação das interfaces, vamos somente chamar o método
    """
    def A(self,s):
        return self.obter_operadores()
    
    """
        Retornar uma probabilidade de transição para todas as transições possiveis
    """
    def T(self,s,a,sn):
        if( sn == self.__transicoes.get((s,a)) ):
            #efetivamente a transição existe
            return 1.0
        else:
            return 0.0
        
        # return 1.0 if sn == self.__transicoes.get((s,a)) else 0.0
    """
        Retornar uma recompensa de transição para todas as transições possiveis
    """
    def R(self,s,a,sn):
        r = -a.custo(s,sn)
        if(sn in self.__objectivos):
            r = r + self.__rmax
        return r
    
    """
        Retornar no formato de uma lista o estado sucessor consoante o estado atual e a acção,
        basicamente faz um get ao dicionário calculado previamente no construtor.
    """
    def Sucessores(self,s,a):
        sn = self.__transicoes.get((s,a))
        return [sn] if sn else []
        
