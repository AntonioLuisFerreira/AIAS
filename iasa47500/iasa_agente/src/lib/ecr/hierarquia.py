from ecr.comport_comp import ComportComp

"""
    A hirarquia é um corportamento composto:
    => Filtra um dos mecanismos de seleção estudados em aula, 
    sendo eles: hierarquia, prioridade e fusão.
"""
class Hierarquia(ComportComp):
    """
        No caso da Hierarquia as primeiras têm mais prioridade dos que vêm a seguir
    """
    def selecionar_accao(self, accoes):
        #verificacao se as ações existem
        if(accoes):
            # return do indice 0 do array de pois as novas accoes são colocadas de forma incremental,
            # logo a accao mais antiga é a que tiver no indice 0.
            return accoes[0]