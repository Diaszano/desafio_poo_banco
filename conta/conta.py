"""Classe das Contas

    A Classe das Contas é uma classe abstrata aonde criaremos o molde de contas
    que queremos seguir nas classes futuras.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from abc import ABC, abstractmethod
#-----------------------
# CLASSES
#-----------------------
class Conta(ABC):
    """Classe das Contas

        A classe contas é uma classe abstrata aonde trataremos de moldar o perfil 
        das classes de contas correntes e poupança.
    """
    __numero_de_conta:int = 0;
    def __init__(self,agencia:int=0,saldo:float=0.0) -> None:
        """Classe das Contas

            Geramos a classe conta.
        """
        self.__agencia:int = agencia;
        self.__saldo:float = saldo;
        self.__gerarConta();
    
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
    def _saldo(self,valor)->None:
        """SETTER Saldo
            
            Alteramos o valor do saldo.
        """
        if isinstance(valor,float):
            self.__agencia = valor;
            return;
        elif isinstance(valor,int):
            self.__agencia = float(valor);
            return;
        raise TypeError(f'Valor não pode ser "{type(valor)}" ele tem que ser [int | float!]');
    
    def __gerarConta(self):
        """Gerador de conta
            
            Geramos contas com valores sequenciais.
        """
        self.__conta += self.__numero_de_conta + 1;

    @abstractmethod
    def depositar(self,valor):
        pass;
    
    @abstractmethod
    def sacar(self,valor):
        pass;
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    a = Conta();
#-----------------------  