"""Classe das Pessoas

    A Classe das Pessoas é uma classe abstrata aonde criaremos 
    o molde de pessoas que queremos seguir nas classes futuras.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from .pessoa import Pessoa
# from ..conta import ContaPoupanca
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Cliente(Pessoa):
    def __init__(   self, nome: str = '', 
                    data_de_nascimento: str = '00/00/0000', 
                    cpf: str = '000.000.000-00') -> None:
        super().__init__(nome, data_de_nascimento, cpf);
        self.contas = None;
        # self.contas     = [];
        # self.__poupanca = False;
        # self.__corrente = False;

    def adicionar_conta(self, conta):
        self.contas = conta;
    
    # @property
    # def poupanca(self):
    #     return self.__poupanca;
    
    # @property
    # def corrente(self):
    #     return self.__corrente;

    # def adicionar_conta(self, conta):
    #     if(len(self.contas) == 0):
    #         self.contas.append(conta);
    #         if(isinstance(conta,ContaPoupanca)):
    #             self.__poupanca = True;
    #         else:
    #             self.__corrente = True;
    #     elif(len(self.contas) == 1):
    #         if(self.__corrente):
    #             if(isinstance(conta,ContaPoupanca)):
    #                 self.__poupanca = True;
    #                 self.contas.append(conta);
    #             else:
    #                 print("Cliente já tem conta Poupança");
    #             return;
    #         else:
    #             if(isinstance(type(conta),ContaPoupanca)):
    #                 self.__corrente = True;
    #                 self.contas.append(conta);
    #             else:
    #                 print("Cliente já tem conta corrente");
    #             return;
    #     print("O cliente já tem conta Corrente e Poupança");
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    pass;
#-----------------------  