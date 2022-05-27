from http import client
from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str = '', data_de_nascimento: str = '00/00/0000', cpf: str = '000.000.000-00') -> None:
        super().__init__(nome, data_de_nascimento, cpf);
        self.contas = [];
    
    def conta(self, conta):
        pass;