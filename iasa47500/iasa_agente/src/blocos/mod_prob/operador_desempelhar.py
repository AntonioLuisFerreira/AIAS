from copy import deepcopy
from blocos.mod_prob.estado_blocos import EstadoBlocos
from blocos.mod_prob.operador_transferir import OperadorTansferir


class OperadorDesempelhar(OperadorTansferir):

    def aplicar(self, estado):

        nova_pilha = estado.pilhas
        
        if nova_pilha[0]:
            pilha = nova_pilha[0].pop(0)
            nova_pilha[self._numero_pilha].insert(0,pilha)
            return EstadoBlocos(nova_pilha)

    
    def __repr__(self):
        return "Desempelhar(%s)" % self._numero_pilha