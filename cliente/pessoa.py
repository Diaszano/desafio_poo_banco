"""Classe das Pessoas

    A Classe das Pessoas é uma classe abstrata aonde criaremos o molde de pessoas
    que queremos seguir nas classes futuras.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from datetime import datetime
from abc import ABC, abstractmethod
#-----------------------
# CLASSES
#-----------------------
class Pessoa(ABC):
    def __init__(   self,nome:str = '',
                    data_de_nascimento:str ='00/00/0000',
                    cpf:str='000.000.000-00'
                ) -> None:
        """Classe Pessoa.
        
            Aqui damos as características principais para os clientes.
        """
        self.__nome       = nome;
        self.__nascimento = data_de_nascimento;
        self.__cpf        = cpf;
        self.__calcula_idade();

    @property
    def nome(self) -> str:
        return self.__nome;
    
    @property
    def data_de_nascimento(self) -> str:
        data = self.__nascimento.replace('/','-');
        return data;
    
    @property
    def cpf(self) -> str:
        return self.__cpf;
    
    @property
    def idade(self) -> int:
        return self.__idade;
    
    def __calcula_idade(self) -> None:
        data_atual      = datetime.now();
        data_atual      = data_atual.strftime('%d-%m-%Y');
        data_atual      = datetime.strptime(data_atual,'%d-%m-%Y');
        data_nascimento = datetime.strptime(self.data_de_nascimento,'%d-%m-%Y');
        idade           = data_atual - data_nascimento;
        idade           = int(idade.days/365);
        self.__idade    = idade;
        print(idade);
    
    @abstractmethod
    def conta(self,conta):
        pass
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    a = Pessoa(nome="Lucas Dias",data_de_nascimento="29/02/2000",cpf='');
#-----------------------  