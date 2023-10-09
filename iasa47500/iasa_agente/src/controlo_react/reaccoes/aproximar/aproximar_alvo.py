from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao

"""
    A Classe AproximarAlvo:
        É o comportamento que vai permitir ao agente aproximar-se de alvos,
        Para generalizar o sistena, vai ser criados comportamentos aproximar para cada uma das 4 direções,
        A prioridade que cada instância tem em relação a distância do agente ao alvo,
        Aproximar Alvo herda de Prioridade e que por sua vez herda de ComportamentoComposto,
        Ao fazer super da classe Comportamento Composto temos de passar uma lista de Comportamentos.
        Os Comportamentos criados são instâncias da classe AproximarDir que recebe uma direção,
        Vendo a documentação existem quatro direções possíveis(NORTE,SUL,ESTE,OESTE),
        Com recurso à compreensão de listas é possível criar um array com as 4 AproximarDir(direção),
        sendo direção in list de direções.
"""
class AproximarAlvo(Prioridade):

    def __init__(self):
        super().__init__([AproximarDir(direccao) for direccao in list(Direccao)])