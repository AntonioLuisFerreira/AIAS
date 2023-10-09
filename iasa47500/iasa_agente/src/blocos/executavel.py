
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from blocos.mod_prob.heur_blocos import HeurBlocos

from blocos.planeador.planeador import Planeador
from blocos.planeador.trajecto import Trajecto


def blocos_exec():

    configuracao_inicial = [[2,3,1],[],[]]
    configuracao_final = [1,2,3]

    procura_custo_uniforme = ProcuraCustoUnif()
    procura_aa = ProcuraAA()

    heur = HeurBlocos(configuracao_final)

    planeador = Planeador()

    solucoes = []

    solucoes.append(planeador.planear(configuracao_inicial,configuracao_final,procura_custo_uniforme))
    solucoes.append(planeador.planear(configuracao_inicial,configuracao_final,procura_aa,heur))
    
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
    

blocos_exec()
"""
O motivo para as duas procuras resultarem soluções iguais é:

O grafo não tem ciclos negativos. Tanto a procura por custo uniforme quanto a procura A* consideram que o grafo não contém ciclos negativos.
Caso contrário, esses algoritmos podem entrar em loops infinitos, pois não há uma solução ótima em um grafo com ciclos negativos.
Portanto, se o grafo for livre de ciclos negativos, tanto a procura por custo uniforme quanto a procura AA podem fornecer os mesmos resultados, encontrando o caminho mais curto.

É de relembrar que procura A* é uma melhoria em relação à outra procura, pois tem a noção de heurística.
A heurística fornece uma estimativa do custo restante para atingir o objectivo a partir de qualquer nó,
permitindo que a procura AA seja mais eficiente em termos de tempo de execução em comparação com a procura por custo uniforme.
Portanto, a procura AA é geralmente preferida quando a heurística de estimativa é aplicável e pode fornecer resultados mais rápidos e eficientes
"""
