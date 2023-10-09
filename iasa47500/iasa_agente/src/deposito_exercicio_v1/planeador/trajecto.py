
class Trajecto():
    def __init__(self,solucao):
        self.__resultado = []
        self.__volumes = [passo.estado.volume for passo in solucao]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    def mostrar(self):
        
        self.tratar_info()

        print('Solução: ', self.__resultado)
        print('Dimensao: ', self.__dimensao)
        print('Custo: ', self.__custo)

    def tratar_info(self):
        result = []
        
        for i in range(1, len(self.__volumes)):
            result.append(self.__volumes[i] - self.__volumes[i-1])
        
        for i in result:
            if i == 2:
                self.__resultado.append('Encher(2)')
            elif i == 3:
                self.__resultado.append('Encher(3)')
            elif i == -2:
                self.__resultado.append('Vazar(2)')
            elif i == -3:
                self.__resultado.append('Vazar(3)')