from sae.simulador import Simulador
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from controlo_delib.controlo_delib import ControloDelib

""" 
    Ficheiro py para teste ao planeamento em espaço de estados (PEE)
"""
#definição do controlo passando o planeador
controlo = ControloDelib(PlaneadorPDM(0.95))
#execução da simulador passando o numero do mapa e o controlo
Simulador(4, controlo).executar()