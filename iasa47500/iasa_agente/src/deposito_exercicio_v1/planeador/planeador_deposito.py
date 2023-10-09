from deposito_exercicio_v1.mod_prob.problema_deposito import ProblemaDeposito

class PlaneadorDeposito():

    def planear(self, ligacoes, loc_inicial, loc_final,mecanismo):
        
        problema = ProblemaDeposito(ligacoes, loc_inicial, loc_final)
        name = type(mecanismo).__name__
        solucao = mecanismo.procurar(problema)
        complexidades = (str(mecanismo.complexidade_espacial), str(mecanismo.complexidade_temporal))
        
        return solucao, name,complexidades
        