class Trajecto():

    def __init__(self,solucao):
        self.__estado_operador = [(passo.estado.pilhas,passo.operador) for passo in solucao ]    
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
    
    def mostrar(self):
        print("Solucao:")
        for i,j in self.__estado_operador:
            if j == None:
                j = " " 
            print(i, " ", j)

        print("\nDimensão: ", self.__dimensao)
        print("Custo: ", self.__custo)
    