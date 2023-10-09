"""
    A classe MecUtil,
    Vai implementar os métodos que iram calcular a utilidade e a utilidade da acção,
    para tal se sucesser vai ser preciso o modelo, gama e delta_max.

    Para isso vai ser preciso simular os vários caminhos de acções que se podem desencadear, cadeia de Markov.
    neste contexto da implementação vai ser auxilidado pelos metódos definidos na interface Modelo PDM.

    O construtor vai receber os fatores de gama e delta_max:
        Gama, fator de desconto no visto de recompensas descontadas, varia entre [0, 1] sendo, 
        preferencialmente, um valor mais aproximado de 1;
        Delta max, critério de paragem de iteração.

    Esta classe fornece, assim, métodos que calculam/avaliam a utilidade (efeito cumulativo da evolução da situação) 
"""
class MecUtil():
    """
        O construtor da classe MecUtil,
        Recebe como parâmetro o modelo, gama e delta_max.
        Guarda os parametros em memória com recurso a variaveis privadas.
        
    """
    def __init__(self,modelo,gama,delta_max):
        self.__modelo = modelo
        self.__delta_max = delta_max
        self.__gama = gama
    
    """
        O método público utilidade:
            Tem como objectivo calcular a utilidade de todos os estados,
            efeito cumulativo da evolução de uma situação.

            Processos efetuados:
                Inicialização da utilidade, um dicionário estado: utilidade (a zeros).
                Iterar o dicionário obtendo a maximização da utilidade da acção,
                varrendo as acções que a este podem ser aplicados.
                Esta iteração é repetida até que a fórmula resulte na forma optima,
                condição reconhecida quando já não há mais alteração Utilidade,
                sendo auxiliado pelas variaveis delta.
                Delta é a variação entre duas iterações, quando o delta obtido for menos que delta máximo.
    """
    def utilidade(self):
        # conjunto de estados reformatação do nome do método
        S = self.__modelo.S 
        # conjunto de acções possiveis para cada estado reformatação do nome do método
        A = self.__modelo.A
        #inicialização da utilidade
        #S() porque está a chamar o método em vez de escrever self.__modelo.S()
        U = {s:0.0 for s in S()} 
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([ self.util_accao(s,a,Uant) for a in A(s)], default=0)
                
                delta = max(delta, abs(U[s] - Uant[s]))
            if(delta <= self.__delta_max):
                break
        return U

    """
        O método público util_accao(),
        vai calcular a utilidade de um único estado, irá ser útil numa tomada de decisões óptimas,
        decidir qual a ação com maior utilidade no futuro,
        a ser aplicada por base num estado.
        As utilidades dos estados podem ser determinados em função das utilidades dos estados sucessores.
    
    """
    def util_accao(self, s, a, U):
        T = self.__modelo.T
        R = self.__modelo.R
        Sucessores = self.__modelo.Sucessores
        return sum(T(s,a,sn) * R(s,a,sn) + self.__gama * U[sn] for sn in Sucessores(s,a))
    