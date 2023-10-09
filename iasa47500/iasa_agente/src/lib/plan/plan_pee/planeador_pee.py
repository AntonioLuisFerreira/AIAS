
from plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega

from plan.plan_pee.plano_pee import PlanoPEE
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.heur_manhattan import HeurManhattan

from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan

"""
    A classe PlaneadorPEE herda de Planeador.

    É composto por um mecanismo de Procura, qualquer um do tipo de pesquisa informada.
    Esta classe prinicipal função de definir o problema passando o modelo do mundo e objectivo mais proximo ao agente,
    em casp do mecanismo de procura necessitar é preciso definir a heuristica neste exmplo define-se HeurDist onde passamos como paramtro o primeiro objectivo.
    Calcular a solução e por fim retornar uma instancia do Objecto PlanoPEE com a solução como parametro
"""
class PlaneadorPEE(Planeador):

    """
        O construtor da classe é onde é definido o mecanismo de procura a ser usado.
    """
    def __init__(self):
        #self.__mec_pee = ProcuraSofrega()
        self.__mec_pee = ProcuraAA()
        self.__opcao = None

    """
        Método auxiliar que permite variar entre diferentes heuristicas.
        Neste caso a HeurManhattan() e HeurDist()(Euclideana) são implementados.
    """
    def setHeur(self,opcao):
        if opcao == 0:
            self.__opcao = "HeurManhattan()"
        

    """
        O método planear recebe um modelo do mundo e uma lista de objectivos com isso:
            vai definir o problema com recurso à classe ProblemaPlan
            vai definir a heuristica com recurso à classe HeurDist
            vai calcular a solução chamando o procurar do mecanismo de procura passando o problema e a heuristica.
            por fim, retorna uma instancia da class PlanoPEE
    """
    def planear(self, modelo_plan, objectivos):
        #problema
        problema = ProblemaPlan(modelo_plan, objectivos[0])
        
        #defines a heuristica
        heur = None
        if(self.__opcao == "HeurManhattan()"):
            print("Heuristica: Distancia de Manhattan")
            heur = HeurManhattan(objectivos[0])
        else:
            print("Heuristica: Distancia de Euclideana")
            heur = HeurDist(objectivos[0])
        
        #retorna o plano
        solucao = self.__mec_pee.procurar(problema,heur)

        #print das complexidades
        complexidades = (str(self.__mec_pee.complexidade_espacial), str(self.__mec_pee.complexidade_temporal))
        print("Complexidade Temporal: ", complexidades[1])
        print("Complexidade Espacial: ", complexidades[0], "\n")
        
        return PlanoPEE(solucao)

    
    