from deposito_exercicio_professor.mod_prob.problema_deposito import ProblemaDeposito
from deposito_exercicio_professor.planeador.trajecto import Trajecto

from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.larg.procura_largura import ProcuraLargura

"""
    Declaração do volume inicial e final
"""
VOL_INICIAL = 0
VOL_FINAL = 9

#Método executavel
def teste_deposito():

    print('    => Volume inicial', VOL_INICIAL, '<=')
    print('    => Volume final', VOL_FINAL, ' <=')

    #inicialização do problema
    problema = ProblemaDeposito(VOL_INICIAL,VOL_FINAL)

    #Instancias de diferentes mecanismos de procura
    procura_custo_uniforme = ProcuraCustoUnif()
    procura_profundidade_iterativa = ProcuraProfIter()
    procura_profundidade_limitada = ProcuraProfLim(4)
    procura_largura = ProcuraLargura()
    
    # No array soluções vai guardar em cada indice um tuple em que tem a solução do mecasnismo de procura e o nome do mecasnismo usado
    solucoes = []
    solucoes.append((procura_custo_uniforme.procurar(problema), procura_custo_uniforme.__class__.__name__))
    solucoes.append((procura_profundidade_iterativa.procurar(problema), procura_profundidade_iterativa.__class__.__name__))
    solucoes.append((procura_profundidade_limitada.procurar(problema), procura_profundidade_limitada.__class__.__name__))
    solucoes.append((procura_largura.procurar(problema), procura_largura.__class__.__name__))
    
    #ciclo for para mostar os valores guardados no array de solucoes
    for solucao, nome in solucoes:
        print('\n', nome)
        trajecto = Trajecto(solucao)    
        trajecto.mostrar()

teste_deposito()