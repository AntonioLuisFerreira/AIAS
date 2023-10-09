from ecr.resposta import Resposta
from sae import Accao

"""
    A classe RespostaMover é uma Resposta:
        Permite movimentar o agente.
        De acordo com o pedido da UC pertende-se simular uma AI de um agente que vagueia por um meio ambiente.
        Como consequente as ações a serem realizadas vão estar interligadas com o movimento dele.    
"""
class RespostaMover(Resposta):

    """
        Encadiamento de construtores.
        Envocar o construtor da super classe passa uma accao com a direcao.
        A Accao vem da biblioteca fornecida
    """
    def __init__(self,direcao):
        super().__init__(Accao(direcao))