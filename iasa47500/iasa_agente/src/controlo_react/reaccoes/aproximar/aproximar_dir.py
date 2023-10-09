from ecr.reaccao import Reaccao
from controlo_react.reaccoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

"""
    A Classe Aproximar Direcional herda de Reação, sendo reação um comportamento simples,
    ao utilizar o super sabemos que temos de passar um estimulo e uma resposta.


"""
class AproximarDir(Reaccao):
    
    """
        O construtor da classe utiliza o método da classe super Reaccao,
        recebe como parametros um estimulo e uma resposta
        
        O objectivo de dar um passo em uma certa direccao, 
        o tipo de resposta tem de gerar uma ação de movimento(RespostaMover) tem de receber um parametro de direcao 
        Tal como para gerar um estimulo de 
    
    """
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))