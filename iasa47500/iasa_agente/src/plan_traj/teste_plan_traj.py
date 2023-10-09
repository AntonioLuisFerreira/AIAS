from plan_traj.planeador.ligacao import Ligacao
from plan_traj.planeador.planeador_trajecto import PlaneadorTrajecto
from plan_traj.planeador.trajecto import Trajecto

from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcurarProfundidade
from pee.larg.procura_largura import ProcuraLargura

#definição de localidade inicial e final
LOC_INICIAL = 'loc-0'
LOC_FINAL = 'loc-4'

# array de ligações existentes
ligacoes = [
    Ligacao('loc-0', 'loc-1', 5),
    Ligacao('loc-0', 'loc-2', 25),
    Ligacao('loc-1', 'loc-3', 12),
    Ligacao('loc-1', 'loc-6', 5),
    Ligacao('loc-2', 'loc-4', 30),
    Ligacao('loc-3', 'loc-2', 10),
    Ligacao('loc-3', 'loc-5', 5),
    Ligacao('loc-4', 'loc-3', 2),
    Ligacao('loc-5', 'loc-6', 8),
    Ligacao('loc-5', 'loc-4', 10),
    Ligacao('loc-6', 'loc-3', 15),
]
"""
    Para motivos de avalição é necessário numa só execução poder-se observar todas as soluções de procura,
    para isso foi necessário inicializar todas as instâncias de Procura,
    definir um planeador é de relembrar que o método planear retorna o nome e a solução para o problema consoante o mecanismo usado.
    um array de soluções,
    à medida que é chamdo o planear do planeador vai se dando append da solução ás soluções.
    Com recurso à classe Trajecto faz-se print dos valores necessários para a avaliação em todas as soluções.
"""
def teste_plan_traj():
    # instancias de diferentes tipos de mecanismos de procura
    procura_custo_uniforme = ProcuraCustoUnif()
    procura_profundidade_iterativa = ProcuraProfIter()
    procura_profundidade_limitada = ProcuraProfLim()
    procura_profundidade = ProcurarProfundidade()
    procura_largura = ProcuraLargura()

    #instancia do planeador
    planeador = PlaneadorTrajecto()
    
    #array onde as soluções vão ser guardadas
    solucoes = []

    #guardar o nome e solução no array
    solucoes.append(planeador.planear(ligacoes, LOC_INICIAL,LOC_FINAL, procura_custo_uniforme))
    solucoes.append(planeador.planear(ligacoes, LOC_INICIAL,LOC_FINAL, procura_profundidade_iterativa))
    solucoes.append(planeador.planear(ligacoes, LOC_INICIAL,LOC_FINAL, procura_profundidade_limitada))
    solucoes.append(planeador.planear(ligacoes, LOC_INICIAL,LOC_FINAL, procura_profundidade))
    solucoes.append(planeador.planear(ligacoes, LOC_INICIAL,LOC_FINAL, procura_largura))
    
    #for para cada iteração do array de soluções
    for nome, solucao, complexidades in solucoes:
        # se existir solucao
        if(solucao != None):
            #print do nome do mecanismo
            print('Mecanismo de Procura ', nome)

            

            #inicialização da classe Trajecto para que possa repartir a informação do Trajecto
            trajecto = Trajecto(solucao)
            #ao chamar o mostrar vai dar print à informção da solução
            trajecto.mostrar()
            print('Complexidades Espacial ', complexidades[0])
            print('Complexidades Temporal ', complexidades[1],'\n')


teste_plan_traj()