from pee.prof.procura_profundidade import ProcurarProfundidade
"""
    A classe procura em profundidade limitada.
    O algoritmo de pesquisa em profundidade é aplicado,
    tendo em conta limite a que a profundidade pode atingir.

    Por si mesma não consegue ser um mecanismo optimo (apesar de resolver o problema da profundidade "infinita").

    A classe herda de procura em profundidade que por sua vez herda de mecanismo de procura,
    é importante ter em noção devido à utilização da claase super().

"""
# procura em profundidade limitada
class ProcuraProfLim(ProcurarProfundidade):

    """
        O construtor da classe guarda numa variavel a profundida máxima,
        com recurso ao setter. 
        init  da classe super neste caso procura em profundidade
    """
    def __init__(self, prof_max = 100):
        super().__init__()
        self.__prof_max = prof_max

    #getter da profundidade maxima
    @property
    def prof_max(self):
        return self.__prof_max
    
    #setter da profundidade maxima
    @prof_max.setter
    def prof_max(self, prof_max):
        self.__prof_max = prof_max
    
    """
        O método expandir tem como objectivo expandir o nó,
        se a sua profundidade for menor que a profundidade máxima da procura
    """
    def _expandir(self, problema, no):
        if( no.profundidade < self.prof_max):
            #utilizar o método expandir da classe MecanismoProcura
            yield from super()._expandir(problema,no)
        
    """
        O método memorizar faz memoriza o nó se não corresponder a um ciclo
    """
    def _memorizar(self, no):
        #verifica o ciclo
        if(self._ciclo(no) == False):
            #insere no inicio da fronteira
            
            #self._fronteira.inserir(no)
            super()._memorizar(no)

        #self._fronteira.inserir(no)
    """
        O método ciclo verifica se o nó corresponde a um ciclo do ramo,
        para isso tem que ir comparar o estado do nó atual com os seus antecessores,
        se sim retorna true else False
    """
    def _ciclo(self, no):
        return no.estado in self.__estados_antecessores(no)
    
    """
        Versão antiga do método ciclo
    """
    # def _ciclo(self,no):
    #     antecessor = no.antecessor
    #     # enquanto houver um antecessor
    #     while antecessor is not None:
    #         #verifica se o estado do antecessor é igual ao estado do nó atual
    #         if(antecessor.estado == no.estado):
                
    #             return True
    #         #atualiza o nó em avaliação
    #         antecessor = no.antecessor
    #     #se sair do while sem return quer dizer que o estado do nó não pertence ao ciclo
    #     return False

    """
        Gerador de estados anteriores, método privado que gera os estados dos nos anteriores.
        Um gerador permite gerar valores sem ter que os guardar em memória
    """
    def __estados_antecessores(self,no):
        antecessor = no.antecessor
        while antecessor is not None:
            yield antecessor.estado
            # mudar a instancia do antecessor para o seu antecessor
            antecessor = antecessor.antecessor
            

    


        


