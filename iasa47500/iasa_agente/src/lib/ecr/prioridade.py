from ecr.comport_comp import ComportComp

"""
    A Prioridade é um corportamento composto:
    => Filtra um dos mecanismos de seleção estudados em aula, 
    sendo eles: hierarquia, prioridade e fusão.
"""
class Prioridade(ComportComp):

    """
        Como de acorodo com UML o método selescionar_accao restorna uma accao,
        sendo esta a accao com maior prioridade da lista de accoes.
    """
    def selecionar_accao(self, accoes):
        #verificacao se as ações existem
        if(accoes):
            # com recurso a funções lambda para realizar transformações
            # passando a accao realizando a transformação para a prioridade da accao
            accao = max(accoes, key = lambda accao: accao.prioridade) 
            return accao