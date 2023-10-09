"""
    A classe solução é uma sequencia de nós.
    A solução de um problema descreve passos, caminhos ou trajetos necessários,
    para alcançar o objectivo desejado a partir do estado incial.
"""
class Solucao():
    
    """
        O construtor da classe inicia um array fazio com o percurso,
        depois enquanto houver um nó antecessor vai inseriri no inicio do array o nó a ser avaliado.
        no_final é a folha
    """
    def __init__(self,no_final):
        self.__percurso = []
        no = no_final
        while no:
            self.__percurso.insert(0,no)
            no = no.antecessor

    """
        É uma property que retorna o tamanho do percurso
    """
    @property
    def dimensao(self):
        return len(self.__percurso)
    
    @property
    def percurso(self):
        return self.__percurso
    
    """
        O método remover vê se o percurso existe se sim retorna o percurso sem posição 0,
        último nó a ter sido inserido.  
    """
    def remover(self):
        if(self.__percurso):
            return self.__percurso.pop(0)

    """
        Iterador adaptado para o percurso;
    """
    def __iter__(self):
        return iter(self.__percurso)
    
    """
        GetItem é para ir ao percurso fazer get da posição consoante o indice passado.
    """
    def __getitem__(self,index):
        return self.__percurso[index]