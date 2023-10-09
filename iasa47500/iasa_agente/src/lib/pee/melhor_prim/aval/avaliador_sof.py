from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
    A classe AvaliadorSofrega herda de AvaliadorHeur,
    logo herda também de avaliador por isso mesmo vai ter de implementar o método prioridade.

    Vai ser usado na classe ProcuraSofrega, e irá ter em conta a própria heuristica.
    Logo vai f(n) = h(n)
"""
class AvaliadorSofrega(AvaliadorHeur):
    """
        O método prioridade,
        vai retornar o resultado de h(estado) da heuristica, 
        usada para inicializar o método de procura que irá utilizar este avaliador.
    """
    def prioridade(self,no):
        # f(n) = h(n)
        return self._heuristica.h(no.estado)