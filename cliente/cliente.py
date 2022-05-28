"""Classe das Pessoas

    A Classe das Pessoas é uma classe abstrata aonde criaremos o molde de pessoas
    que queremos seguir nas classes futuras.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from .pessoa import Pessoa
#-----------------------
# CLASSES
#-----------------------
class Cliente(Pessoa):
    def __init__(self, nome: str = '', data_de_nascimento: str = '00/00/0000', cpf: str = '000.000.000-00') -> None:
        super().__init__(nome, data_de_nascimento, cpf);
        self.contas = [];
    
    def conta(self, conta):
        pass;
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    a = Pessoa(nome="Lucas Dias",data_de_nascimento="29/02/2000",cpf='');
#-----------------------  