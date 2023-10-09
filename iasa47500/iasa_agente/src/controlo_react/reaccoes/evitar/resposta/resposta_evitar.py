import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao

"""
    A Classe RespostaEvitar herda de RespostaMover,
    tem que responder uma direcao para o agente evitar um obstaculo detetado no meio ambiente.


"""
class RespostaEvitar(RespostaMover):

    """
        O construtor da classe tem como parêmtro a direção iniciar que vai passar,
        ao método super da classe RespostaMover, se não for passado nada a direção inicial por default,
        Direcao.ESTE.
        Tem uma váriavel privada composta por uma lista das Direções (NORTE,SUL,ESTE,OESTE)

    """
    def __init__(self, dir_inicial = Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = list(Direccao)

    
    """
        O método activar vê se há contacto com obstacuçp 
    """
    def activar(self,percepcao, intensidade):

        contacto_obst = percepcao.contacto_obst(self._accao.direccao)

        if contacto_obst:
            contacto_obst = not self.__alterar_direccao(percepcao)

        if not contacto_obst:
            return  super().activar(percepcao,intensidade)

    """
        Escolhe uma direcao livre
    """
    def __direccao_livre(self,percepcao):

        direccoes_livres = [direccao for direccao in self.__direccoes
                            if not percepcao.contacto_obst(direccao)]  
        
        return random.choice(direccoes_livres)
    
    """
        Altera a direccao para outra direccao livre aleatoria
    """
    def __alterar_direccao(self,percepcao):
        # Armazena uma direccao livre para depois substituir
        direccao_livre = self.__direccao_livre(percepcao)
        #Verifica se a direccao livre é diferente de None
        if(direccao_livre != None):
            # Altera de facto a direção para a direção livre gerada pelo método 
            # privado direção livre
            self._accao.direccao = direccao_livre
            return self._accao.direccao
