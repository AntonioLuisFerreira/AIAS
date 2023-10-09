from sae.simulador import Simulador
from plan.plan_pee.planeador_pee import PlaneadorPEE
from controlo_delib.controlo_delib import ControloDelib

from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.heur_manhattan import HeurManhattan

""" 
    Ficheiro py para teste ao planeamento em espaço de estados (PEE)
"""
for i in range(2):
    #definição do planeador
    planeador = PlaneadorPEE()
    #faz set da heur
    planeador.setHeur(i)
    #definição do controlo passando o planeador
    controlo = ControloDelib(planeador)
    #execução da simulador passando o numero do mapa e o controlo
    Simulador(4, controlo).executar()

"""
Observação de Resultados:

Heuristica: Distancia de Manhattan
Complexidade Temporal:  202
Complexidade Espacial:  226 

Heuristica: Distancia de Manhattan
Complexidade Temporal:  420
Complexidade Espacial:  233 

Heuristica: Distancia de Manhattan
Complexidade Temporal:  807
Complexidade Espacial:  426 

Heuristica: Distancia de Euclideana
Complexidade Temporal:  230
Complexidade Espacial:  247 

Heuristica: Distancia de Euclideana
Complexidade Temporal:  463
Complexidade Espacial:  247 

Heuristica: Distancia de Euclideana
Complexidade Temporal:  882
Complexidade Espacial:  438 


A heurística de distância de Manhattan apresenta uma complexidade temporal menor em comparação com a heurística de distância euclidiana.
Isso indica que a heurística de Manhattan encontra soluções mais rapidamente para os problemas da busca.

Já em relação à complexidade espacial, a heurística de distância de Manhattan também tende a ter valores menores do que a heurística euclidiana.
Logo, sugere que a heurística de Manhattan exige menos espaço de armazenamento durante o processo de busca.

Por fim, pode-se admitir que a heurística da distância de Manhattan é mais eficiente tanto em termos de tempo quanto de espaço em comparação com
a heurística de distância euclidiana no contexto do algoritmo de ProcuraAA.

"""