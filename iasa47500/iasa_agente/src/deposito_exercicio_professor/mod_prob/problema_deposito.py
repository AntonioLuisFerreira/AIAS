from deposito_exercicio_professor.mod_prob.operador_encher import OperadorEncher
from deposito_exercicio_professor.mod_prob.operador_vazar import OperadorVazar
from mod.problema.problema import Problema
from mod_prob.estado_deposito import EstadoDeposito


class ProblemaDeposito(Problema):

    """
        O construtor da classe vai o volume inicial e final
        o construtor da classe super vai recebre o estado do volume inicial e o um array com os operadores possíveis.
        guarda o estado do volume final numa variavel privada
    """
    def __init__(self, vol_inicial, vol_final):

        super().__init__(EstadoDeposito(vol_inicial), [OperadorEncher(2),OperadorEncher(3),OperadorVazar(2),OperadorVazar(3)])

        self.__volume_final = EstadoDeposito(vol_final)

    """
        O método objectivo é quando o volume a ser proccesado for igual ao volume final.
    """
    def objectivo(self, volume):
        return volume == self.__volume_final