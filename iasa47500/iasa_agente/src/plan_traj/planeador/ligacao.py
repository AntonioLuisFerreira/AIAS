from dataclasses import dataclass

"""
    A Dataclass ligação,
    Vai representar cada linha da tabela que representa o problema que será tratado na execução.

    A classe Ligação incapsula a informação de origem de destino e o custo da ligação.
    Neste contexto, a identificação de um estado, do seu sucessor e do seu custo da aplicação de operador,
    que permita transitar do primeiro para o segundo.
"""
@dataclass
class Ligacao():
    origem: str
    destino: str
    custo: int