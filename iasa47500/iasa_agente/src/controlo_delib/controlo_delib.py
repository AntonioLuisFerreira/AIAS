from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo

from sae.agente.controlo import Controlo

"""
    A classe ControloDelib herda da classe Controlo da biblioteca SAE fornecida pelo Docente da UC:
    Este tipo de controlo, o agente vai ter uma memória do passado tanto como previsão do futuro.
    A memória tem o seguinte funcionamento:
        previsão do futuro vai ser gerado com base na memória passada;
        destas previsões vão ser geradas acções à percepcão presente detetada pelo agente.
    
    O prucesso vai ser:
        observar o meio (mundo), obtém percepções (o que rodeia o agente);
        vai atualizando a percepção do mundo;
        calculada as opções que podem ser tomadas, prevendo possíveis fins;
        assimilia e planea a acção a tomar;
        por fim executa a acção.

    É importante frisar que a possível consequência do processo implementado,
    se o mundo sofrer alteraçôes ao longo do tempo o agente irá demorar a chegar a uma possível resposta.
    Por este motivo no processamento antes de executar há uma reconsideração da acção a ser executada.    
"""
class ControloDelib(Controlo):

    """
        O construtor da classe:
            recebe como parametro um planeador que vai ser guardado numa variavel privada,
            inicializa uma referencia de objectivos e de plano a None,
            inicializa um objecto da classe ModeloMundo (mapa por onde o agente irá navegar)
            inicializa um objecto da classe MecDelib passando como paramento o modelo do mundo
    """
    def __init__(self,planeador):
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__objectivos = None
        self.__plano = None

    """
        O método processar recebe uma percepção e irá retornar uma acção.
        É composto por:
            assimilar a percepção recebida
            verficar se é necessário reconsiderar
            em caso de afirmativo vai deliberar e planear
            mostra
            e por fim executa (retorna uma acção)
        
        Os métodos seguintes desta classe permitem implmentar a função de cada processo de tomada de decisão.
        O método processar consiste na ativação desses métodos.
    """
    def processar(self, percepcao):
        #assimila, actualiza o modelo do mundo com a percepção
        self.__assimilar(percepcao)        
        #reconsidera
        if self.__reconsiderar():
            #a deliberação no fundo vai actualizar a lista de objectivos
            self.__deliberar()
            # o planear, cria um plano de acordo com o planeador passando o modelo do mundo e os objectivos
            self.__planear()
        # mostra os resultados na janela pygame
        self.__mostar()
        #o executar retorna uma acção
        return self.__executar()

    """
        O método privado assimilar recebe uma percepção,
        e vai actualizar o modelo do mundo com ela,
        resultando numa actualização da representação do modelo do mundo.
    """
    def __assimilar(self,percepcao):
        self.__modelo_mundo.actualizar(percepcao)

    """
        O método privado reconsiderar tem como objectivo verificar se a representação actual do mundo foi alterada,
        Para ver se mundo foi alterada basta ver a property alterado do mundo onde vai indicar se sim ou não.
    """
    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano

    """
        O método privado deliberar vai actualizar os objectivos com recurso ao mecanismo de deliberação.
    """
    def __deliberar(self):
        #atualizar os objectivos do agente
        self.__objectivos = self.__mec_delib.deliberar()
    
    """
        O método privado planear tem como principal objectivo de activar o planear do planeador,
        e guardar a informação na variavel privada plano definida no construtor da classe.
        Essa mesma activação só é feita de existir objectivos,
        pois no caso de não haver obejctivos o plano mantém-se inalterado,
        e assim não dá erro na execução do programa.
    """
    def __planear(self):
            if(self.__objectivos):
                self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
            else:
                self.__plano = None
        

    """
        O método privado executar tem como objectivo executar retorna uma accao.
        Para o método retornar uma acção tem de verificar se existe plano e objectivos,
        caso afirmativo chama o método obter acção do plano onde passa o estado do modelo do mundo.
        O obter accao retorna um operador e como necessário uma accao chama-se a property do operador 'accao'.
    """
    def __executar(self):
        if(self.__plano and self.__objectivos):
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            return operador.accao
        
    
    """
        O método privado mostrar vai permitir ter uma representação visual do que está a acontecer,
        vai mostar os obstaculos, alvos e posição do agente na janela pygame do executável.
    """
    def __mostar(self):
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if(self.__plano):            
            self.__plano.mostrar(self.vista)
            self.vista.mostrar_estados(self.__objectivos)
            