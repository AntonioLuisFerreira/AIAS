from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur
"""
    A classe AvaliadorAA herda de AvaliadorHeur.
    Vai ser utilizado na Classe de ProcuraAA , vai ter como objectivo minimizar o custo de exploração.
    O resultado irá ser sempre inferior ou igual ao custo efectivo mínimo.
"""
class AvaliadorAA(AvaliadorHeur):
    """
        O método prioridade,
        Vai retornar a soma do custo do nó com o resultado do método h() da heuristica usada,
        para inicializar o método de procura de procura que utiliza o avaliadorAA
    """
    def prioridade(self,no):
        # f(n) = g(n) + h(n)
        return no.custo + self._heuristica.h(no.estado)