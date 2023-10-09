from abc import ABC, abstractclassmethod

"""
    Class Estimulo é uma interface

    Vai permitir a intensidade de determinado dado do ambiente

    Com observação do diagrama UML:
        diz que declara um método abstrato que recebe uma percepcao
        da return à intensidade de um dado do ambiente

    Em base na percepção, ao chamar o método detectar, a interface vai obter
    a intensidade de uma caracteristica do ambiente, vai ser necessário reconhecer a resposta do agente.

"""
class Estimulo(ABC):

    """
        O método detectar é um método abstrato para outras classes que extendem Estimulo usarem esse método.
        Tem como parametro self devido às caracteriscas das Classes em Python.
    """
    @abstractclassmethod
    def detectar(self, percepcao):
        """
            Detetar estimulo em uma percepção
        """