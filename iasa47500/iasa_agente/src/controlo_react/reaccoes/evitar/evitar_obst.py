from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


"""
    A Classe Evitar Obstaculo herda de Hierarquia logo é um comportamento composto.
    Vai ter uma resposta expecifica para evitar obstaculo detetado
    
"""
class EvitarObst(Hierarquia):
    """
        Para além de armazenar numa varável a RespostaEvitar.
        Utiliza método super da classe Comportamento Composto,
        logo tem de receber uma lista de comportamentos, os comportamentos a serem passados,
        Evitar Direções com as direcoes e a resposta evitar armazenada previamente
        
    """
    def __init__(self):
        resposta = RespostaEvitar()
        super().__init__([EvitarDir(direcao,resposta) for direcao in list(Direccao)])