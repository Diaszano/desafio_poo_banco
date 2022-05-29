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
        self.__clientes            = [];
        self.__contas              = [];

    @property
    def agencia(self)->int:
        return self.__agencia;
    
    @property
    def nome(self)->str:
        return self.__nome;

    @property
    def clientes(self)->list:
        return self.__clientes;

    @property
    def contas(self)->list:
        return self.__contas;
    
    @nome.setter
    def _nome(self,nome)->str:
        if(not isinstance(nome,str)):
            raise ValueError((  f"O nome precisa ser um str "
                                f"não um {type(nome)}"));
        self.__nome = nome;
    
    def adicionar_cliente(self,cliente)->None:
        self.__clientes.append(cliente);
    
    def adicionar_contas(self,contas)->None:
        self.__contas.append(contas);

    def autenticar(self,cliente)->bool:
        if cliente not in self.clientes:
            return False;
        if cliente.contas not in self.contas:
            return False;
        if cliente.contas.agencia != self.agencia:
            return False;
        return True;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#----------------------- 
if(__name__ == "__main__"):
    pass;
#-----------------------