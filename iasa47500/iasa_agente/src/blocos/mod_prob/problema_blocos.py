from mod.problema.problema import Problema
from blocos.mod_prob.operador_empelhar import OperadorEmpelhar
from blocos.mod_prob.operador_desempelhar import OperadorDesempelhar
from blocos.mod_prob.estado_blocos import EstadoBlocos

class ProblemaBlocos(Problema):

    def __init__(self, configuracao_inicial , configuracao_final):
        self.__operadores = [OperadorEmpelhar(1),OperadorEmpelhar(2),OperadorDesempelhar(1),OperadorDesempelhar(2)]
        super().__init__(EstadoBlocos(configuracao_inicial),self.__operadores)
        self.__configuracao_final = configuracao_final

    def objectivo(self, estado):
        return estado.pilhas[0] == self.__configuracao_final