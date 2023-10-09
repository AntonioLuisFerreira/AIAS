from pee.prof.procura_prof_lim import ProcuraProfLim
"""
    A classe Procura Iterativa, herda de ProcuraProfLim que por sua vez herda de ProcuraProfundidade
    É um tipo de procura em profundidade.

    Esta tipo de procura vai solucionar principais desafios da pesquisa em profundidade.
    Com junção ao mecanismo de pesquisa em profundidade limitada,
    aplica o algoritmo procura a profundidades sequencialmente até que se chegue ao objectivo.
"""
#procura em profundidade iterativa
class ProcuraProfIter(ProcuraProfLim):

    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        #retorna uma solução
        profundidade = 0
        while(profundidade <= limite_prof):
            
            #setter da profundidade para ser utilizado pelo expandir e memorizar do procura limitada 
            self.prof_max = profundidade
            # chamar o super.procurar e passar o problema retorna uma solução

            solucao = super().procurar(problema)
            
            #iterar a profundidade 
            profundidade = profundidade + inc_prof
            
            #se a solução não for none dá return da solução
            if(solucao != None):
                return solucao
        #se não fizer nada retorna None
        return None
    

    """
        Versão procurar feita pelo docente na aula
        
    """
    # def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        
    #     for profundidade in range(0,limite_prof +1, inc_prof):
            
    #         self.prof_max = profundidade
    #         solucao = super().procurar(problema)
    #         if solucao != None:
                
    #             return solucao
        
        

