from mod.operador import Operador
from sae.agente.accao import Accao
from mod.agente.estado_agente import EstadoAgente
import math as m

"""
    A classe OperadorMover herda da classe Operador:
    Vai representar um movimento que o agente pode efectuar par ir de uma posicao para outra.
    Logo, vai ser inicializado com um certo angulo.
    A aplicação de um vector com esse angulo e dada distância na posição que dado estado vai representar,
    vai equivaler na posição do estado sucessor.

    Irá também guardar uma instancia do modelo do mundo para garantir que os estados que se obtém existem mesmo.
"""
class OperadorMover(Operador):
    """
        O construtor da classe recebe um modelo do mundo e uma direcao,
        guarda o parametro modelo_mundo numa variavel privada,
        já o angulo resulta de um valor da direccao recebida como parametro
        e a accao é uma instancia da classe Accao que recebeu como param a direccao do construtor.        
        É de relembrar que a direccao é uma enumeração
    """
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

    #getter do ang
    @property
    def ang(self):
        return self.__ang

    #getter da accao
    @property
    def accao(self):
        return self.__accao
    
    """
        O método aplicar caso possível um estado sucessor,
        Sendo cada estado representativo de uma posição,
        e o operador uma representação de um movimento em dado ângulo,
        a posição que o novo estado vai se obter aplicando o movimento pelo vetor na posição
        que o estado enviado representa.

        Por fim, retorna-se caso o estado exista no contexto do modelo do mundo.

    """
    def aplicar(self,estado):

        x, y = estado.posicao
        
        dx = round(self.accao.passo * m.cos(self.ang))
        dy = round((-1*self.accao.passo) * m.sin(self.ang))

        nova_posicao = (x+dx, y+dy)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado 


    """
        O método custo irá retornar o custo da aplicação do operador,
        usando o dist da biblioteca math calcula-se a distância entre a posição do estado atual de com a do sucessor.
        se for menor que 1 retorna 1.
    """
    def custo(self, estado, estado_suc):
        # dist =  m.dist(estado.posicao,estado_suc.posicao)
        # return dist if dist > 1 else 1
        return max(1, m.dist(estado.posicao,estado_suc.posicao))