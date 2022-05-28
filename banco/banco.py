"""Classe do Banco"""
#-----------------------
# BIBLIOTECAS
#-----------------------
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Banco():
    __numero_da_agencia: int = 1;
    def __init__(self,nome:str="Banco Do Brasil") -> None:
        self.__nome                = nome;
        self.__agencia             = self.__numero_da_agencia;
        Banco.__numero_da_agencia += 1;

    @property
    def agencia(self):
        return self.__agencia;
    
    @property
    def nome(self):
        return self.__nome;
    
    @nome.setter
    def _nome(self,nome):
        if(not isinstance(nome,str)):
            raise ValueError((  f"O nome precisa ser um str "
                                f"não um {type(nome)}"));
        self.__nome = nome;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#----------------------- 
#-----------------------