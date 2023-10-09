"""
    Um nó é uma estrutura de dados representado por o estado de um problema,
    pode incluir informações do estado atual, caminho percorrido para alcançá-lo,
    custo total e profundidade.
    Numa etapa de busca este algoritmo expande sucessivamente os nós,
    originando novos nós a partir de ações (possíveis em cada estado).
    
    Cada nó expandido é adicionado em uma lista de nós expandidos,
    e o algoritmo decide qual o nó será expandido a seguir tendo em conta cada tipo de procura,
    que leva em consideração o custo total até o momento.
    
    Pode-se dizer que o nó é uma peça fundamental no processo de busca,
    porque contém todoas as informações necessárias para o algoritmo proliferar (resolução de problemas).
    Tem como objectivo localizar o nó que representa o estado final do problema.
"""
class No():
    
    """
        O construtor da classe nó, tem duas maneiras de ser instanciado;
        
        => um nó raiz, que não tem antecessores, apenas o estado que representa,
        por omissão o custo e a profundidade são 0.

        => um dos restantes nós de procura, com informação sobre o operardor e o antecessor,
        o custo será a soma do custo do nó anterior com o custo da aplicação do operador,
        a profundidade será 1 valor superior à do antecessor.
    """
    def __init__(self, estado, operador = None, antecessor = None):
        self.__estado     = estado
        self.__operador   = operador
        self.__antecessor = antecessor

        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
            self.__custo        = antecessor.custo + operador.custo(antecessor.estado, estado)
        else:
            self.__profundidade = 0
            self.__custo = 0.
        
    """ 
        Read Only :
            É de relembrar que @property torna visiveis variaveis privados, 
            e só tem getter e não setter. 
    """
    @property
    def profundidade(self):
        return self.__profundidade
    @property
    def custo(self):
        return self.__custo
    @property
    def antecessor(self):
        return self.__antecessor
    @property
    def estado(self):
        return self.__estado
    @property
    def operador(self):
        return self.__operador
    
    """
        O método __lt__(), less than é chamdo quando se usa <,
        um nó é considerado menor que o outro se o custo for menor.
    """
    def __lt__(self,no):
        return self.__custo < no.custo