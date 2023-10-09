from pee.melhor_prim.aval.heuristica import Heuristica


class HeurBlocos(Heuristica):

    def __init__(self,configuracao_final):
        self.__config_final = configuracao_final
           
    def h(self, estado):
        dif = 0
        if len(estado.pilhas[0]) != len(self.__config_final):
            dif = len(self.__config_final) - len(estado.pilhas[0])
        # print("diferenca: ", dif)
        h = sum(1 for a,b in zip(self.__config_final, estado.pilhas[0]) if a != b) + dif
        # print("Configuração final",self.__config_final)
        # print("estado.pilhas[0]",estado.pilhas[0])
        # print("h", h)
        return h