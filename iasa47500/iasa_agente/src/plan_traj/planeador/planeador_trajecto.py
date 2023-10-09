from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj

"""
    A classe PlaneadorTrajecto é a classe que vai permitir verificar a implementação da biblioteca pee,
    o objectivo é criar um planeador de trajectos entre duas localidades.
    O método de procura do melhor trajeto será alterado mediante testes,
    passado como paramentro do método planear.
"""
class PlaneadorTrajecto():
    """
        O método publico planear recebe como parametros ligaçoes a localidade inicial e final e o tipo de mecanismo que irá iniciar a procura.
        Este método retorna o nome do mecanismo e a solucao incapsulados num tuple.

        Para definir um problema é necessário chamar a classe ProblemaPlanTraj,
    """
    def planear(self, ligacoes, loc_inicial, loc_final,mecanismo):
        # criação do problema passando as ligações as localidades inicial e final
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        # nome do mecanismo de procura a ser usado
        nome = type(mecanismo).__name__
        # a solução é resultante de chamar o procurar do mecanismo passando o problema
        solucao = mecanismo.procurar(problema)        
        
        complexidades = (str(mecanismo.complexidade_espacial), str(mecanismo.complexidade_temporal))
                
        return nome, solucao, complexidades
        