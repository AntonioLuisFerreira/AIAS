from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from sae.ambiente.direccao import Direccao
from math import dist
from plan.modelo.modelo_plan import ModeloPlan

"""
    A classe ModeloMundo herda da interface ModeloPlan:

    Vai representar o mundo em que o agente irá navegar, vai ser actualizado ao longo do tempo.
    Permite fazer a simulação do futuro através da aplicação de operadores (capazes de reconhecer possível fins).
    Nesta classe vai ser inicializado um conjunto de atributos que vão ser ser importantes para a implementação do modelo do mundo.
    Vai ter um dicionário que para cada posição do mundo vai dizer que elemento representa, bem como listas de operadores e estados.
    (EstadoAgente e OperadorMover respetivamente).
    
"""
class ModeloMundo(ModeloPlan):
    """
        O construtor da classe inicializa:
            o estado a None;
            lista de estados vazia;
            o dicionário de elementos vazio;
            uma lista de operadores com as quatro direções na Enumeração Direccao;
            uma flag alterado a false.
    """
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {} # elementos é um map logo tem de ser um dicionário
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__alterado = False

    #getter de alterado
    @property
    def alterado(self):
        return self.__alterado
    
    #getter de elementos
    @property
    def elementos(self):
        return self.__elementos
    
    """
        Retorna o estado actual no modelo do mundo
    """
    def obter_estado(self):
        return self.__estado

    """
        Retorna uma lista de estados no domínio do modelo do mundo.
    """
    def obter_estados(self):
        return self.__estados

    """
        Retorna uma lista de operadores no domínio do modelo do mundo.
    """
    def obter_operadores(self):
        return self.__operadores

    """
        O método obter elemto, 
        retorna o elmento do dicionário (posição:elemento),
        na chave de posição do método enviado para a função.
    """
    def obter_elemento(self,estado):
        #é utilizado o get, pois em caso de usar [] se a key não existir iria causar uma excepção. 
        return self.__elementos.get(estado.posicao)

    """
        O método distancia com recurso ao dist vai calcular a distancia
        entre a posicao do estado recebido como parametro
        e a posicao do estado guardado na variavel da classe.
    """
    def distancia(self,estado):
        return dist(estado.posicao, self.__estado.posicao)
    
    """
        O método actualizar:
            Vai aplicar o processo da actualizar o modelo do mundo.
            Começa por actualizar o estado actual com base na posicao da percepção recebida como parametro.
            Verifica que os elementos percepcionados são iguais aos guardados.
            Em caso:
                Negativo, atualiza os elementos
                          atualiza estados criando, para este último, um objeto EstadoAgente com cada posição percepcionada
                          e muda a flag para true;
                Afirmativo, coloca a flag a false
    """
    def actualizar(self,percepcao):
        #actualizar o estado
        self.__estado = EstadoAgente(percepcao.posicao)

        if self.__elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False

    """
        O método mostrar recebe como parametro a vista
        O objectivo é visualizar os alvos e obstáculos bem como a posição do agente
        Utiliza os métodos da bibioteca SAE classe Visualização.
    """
    def mostrar(self,vista):
        vista.limpar()
        vista.mostrar_alvos_obst(self.__elementos)
        vista.marcar_posicao(self.__estado.posicao)