from sae import Direccao
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento

"""
O método choices() retorna vários elementos aleatórios da lista com reposição.
Os elementos podem ser uma string, um intervalo, uma lista, um tuplo ou qualquer outro tipo de sequência.
"""
from random import choice

"""

A Classe Explorar:
    A classe Explorar é um Comportamento.

    Vai permitir ao agente vaguear pelo meio ambiente, de forma aleatória.

    A classe vai tratar o explorar como gerar movimentos aleatórios. 
    
    O objectivo do comportamento do agente será num futuro recolher alvos,
    aproximar dos alvos, evitar obstáculos e por fim explorar(vaguear pelo ambiente).


"""
class Explorar(Comportamento):

    """
        O activar tem de gerar uma accao numa direcção aleatoria,
        com a direcao pode-se gerar uma resposta mover
        para activar uma resposta basta passar a percepção,
        recordando que a intensidade está como default estar a 0.
    """
    def activar(self, percepcao):

        # Para gerar uma direcao aleatoria
        # Para tal se suceder temos de converter o enumerado para uma lista,
        # o enumerado são as 4 direções  da rosa dos ventres.
        direccao = choice(list(Direccao))
        
        #passa a direcao escolhida à resposta
        resposta = RespostaMover(direccao)
        
        #por sua vez faz a sua ativação da resposta
        return resposta.activar(percepcao)