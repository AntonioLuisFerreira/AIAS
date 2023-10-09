from deposito_exercicio_v1.planeador.ligacao_deposito import Ligacao
from deposito_exercicio_v1.planeador.planeador_deposito import PlaneadorDeposito
from deposito_exercicio_v1.planeador.trajecto import Trajecto

from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcurarProfundidade
from pee.larg.procura_largura import ProcuraLargura

VOL_INICIAL = 0
VOL_FINAL = 9

ligacoes = [
    Ligacao('Vazar-3', 9),
    Ligacao('Encher-2', 4),
    Ligacao('Vazar-2', 4),
    Ligacao('Encher-3', 9)
    
]

def teste_deposito():
    print('    => Volume inicial', VOL_INICIAL, '<=')
    print('    => Volume final', VOL_FINAL, ' <=')

    procura_custo_uniforme = ProcuraCustoUnif()
    procura_profundidade_iterativa = ProcuraProfIter()
    procura_largura = ProcuraLargura()
    procura_profundidade_limitada = ProcuraProfLim(10)
    planeador = PlaneadorDeposito()

    solucoes = []
    
    solucoes.append(planeador.planear(ligacoes, VOL_INICIAL,VOL_FINAL, procura_custo_uniforme))
    solucoes.append(planeador.planear(ligacoes, VOL_INICIAL,VOL_FINAL, procura_profundidade_limitada))
    solucoes.append(planeador.planear(ligacoes, VOL_INICIAL,VOL_FINAL, procura_profundidade_iterativa))
    solucoes.append(planeador.planear(ligacoes, VOL_INICIAL,VOL_FINAL, procura_largura))
    
    for solucao, name, complexidades in solucoes:
        print('Mecanismo de Procura: ', name)
        trajecto = Trajecto(solucao)    
        trajecto.mostrar()
        print('Complexidades Espacial ', complexidades[0])
        print('Complexidades Temporal ', complexidades[1],'\n')


teste_deposito()