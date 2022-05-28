"""Classe das Contas

    A Classe das Contas é uma classe abstrata aonde criaremos o molde 
    de contas que queremos seguir nas classes futuras.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from random import randint
from abc import ABC, abstractmethod
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Conta(ABC):
    """Classe das Contas

        A classe contas é uma classe abstrata aonde trataremos de 
        moldar o perfil das classes de contas correntes e poupança.
    """
    __proxima_conta: int = 1;
    def __init__(self,agencia:int=0,saldo:float=0.0) -> None:
        """Classe das Contas

            Geramos a classe conta.
        """
        self.__agencia:int     = agencia;
        self.__saldo  :float   = saldo;
        self.__conta  :int     = self.__proxima_conta;
        Conta.__proxima_conta += 1;
    
    @property
    def agencia(self)->int:
        """GETTER Agência
            
            Pegamos o número da conta.
        """
        return self.__agencia;
    
    @property
    def saldo(self)->float:
        """GETTER Saldo
            
            Pegamos o valor do saldo.
        """
        return round(self.__saldo,2);
    
    @saldo.setter
    def _saldo(self,valor:float)->None:
        """SETTER Saldo
            
            Alteramos o valor do saldo.
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico");
        self.__saldo = valor;
    
    @property
    def conta(self):
        return self.__conta;

    @abstractmethod
    def depositar(self,valor):
        pass;
    
    @abstractmethod
    def sacar(self,valor):
        pass;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    pass;
#-----------------------  