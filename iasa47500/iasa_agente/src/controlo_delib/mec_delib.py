from sae.ambiente.elemento import Elemento
"""
    A classe MecDelib:
        vai gerar os objectivos do agente com recurso ao modelo do mundo,
        com o modelo do mundo vai se obter os estados em que o elemnto seja um alvo,
        e esses serão os objectivos.
        Em caso de haver objectivos vai se fazer uma ordenação de acordo com a distância.
"""
class MecDelib():
    
    """
        O construtor da classe recebe um modelo do mundo,
        e guarda numa variavel privada
    """
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
    
    """
        O método deliberar consiste em deliberar e retornar os objectivos em caso de existirem.
        Para haver a determinação dos objectivos é necessario para estado no modelo do mundo é preciso verificar se o elemto desse estado é do tipo ALVO,
        se sim é colocado na lista de objectivos se não são ignorados,
        depois de criar a lista de objectivos têm se ordernar os objectivos por distancia mais perto ao agente.
        E por fim retornar a lista de objectivos.
    """
    def deliberar(self):
        #a lista de objectivos é uma lista de estados
        objectivos = [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        #verificar se existem objectivos
        if objectivos:
            #organizar a lista de objectivos de acordo com a distancia
            objectivos.sort(key = self.__modelo_mundo.distancia)
            #retornar a lista de objectivos
            return objectivos
    
    