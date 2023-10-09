from sae.simulador import Simulador
from ecr.prioridade import Prioridade

from controlo_react.controlo_react import ControloReact
#from controlo_react.reaccoes.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher

"""
    Execução do modulo de teste onde vai aplicar o Recolher
    Tem como objectivo recolher dados do meio ambiente (e.g Obstaculos) 
    Utilizando um comportamento composto 
    
"""
# Activação

#Requesito usar um comportamento composto onde usa o comportamento Explorar
#comportamentos = [Explorar()]

# Como definido um Comportamento Composto utilza um array de comportamentos,
# e retorna um comportamento a ser usado.
# Assim com as condições conseguidas pode-se chamar o controlo reac com o comportamento resultante

# guardando numa variavel o controlo_react
# pode-se por fim chamar a Classe Simulação, passar a variavel do controlo react,
# e executar.
#controlo_react = ControloReact(Prioridade(comportamentos))

#testar o controloReact mas agora o agente consegue recolher dados do ambiente
controlo_react = ControloReact(Recolher())

Simulador(1, controlo_react).executar()