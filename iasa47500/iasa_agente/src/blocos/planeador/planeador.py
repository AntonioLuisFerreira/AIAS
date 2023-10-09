from blocos.mod_prob.problema_blocos import ProblemaBlocos

class Planeador():

    def planear(self, configuracao_inicial , configuracao_final, mecanismo, heur = None):

        problema = ProblemaBlocos(configuracao_inicial, configuracao_final)

        nome = type(mecanismo).__name__

        if(nome == "ProcuraCustoUnif"):
            solucao = mecanismo.procurar(problema)            
        else:
            solucao = mecanismo.procurar(problema,heur)

        complexidades = (str(mecanismo.complexidade_espacial), str(mecanismo.complexidade_temporal))
                
        return nome, solucao, complexidades