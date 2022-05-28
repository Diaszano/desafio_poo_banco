"""Classe das Contas Correntes

    A Classe das Contas correntes é uma classe aonde criaremos as 
    contas correntes dos users.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from .conta import Conta
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class ContaCorrente(Conta): 

    __custo_deposito: float = 5.50;
    __custo_saque   : float = 7.50;
    
    def __init__(   self, agencia: int = 0, saldo: float = 0,
                    limite:float = 100.0) -> None:
        super().__init__(agencia, saldo);
        self.__limite = limite;
    
    def __str__(self):
        mensagem:str = f"Conta: {self.conta} Agência: {self.agencia}\n";
        mensagem    += f"Saldo da conta: R${self.saldo}\n";
        mensagem    += f"Limite da conta: R${self.limite}\n";
        return mensagem;
    
    @property
    def custo_saque(self)->float:
        return self.__custo_saque;
    
    @property
    def custo_deposito(self)->float:
        return self.__custo_deposito;

    @property
    def limite(self)->float:
        return round(self.__limite,2);
    
    @limite.setter
    def _limite(self,valor)->None:
        if(isinstance(valor,int) or isinstance(valor,float)):
            self.__limite += valor;
            return;
        raise TypeError((   f'Valor não pode ser "{type(valor)}" '
                            'ele tem que ser [int | float!]'));
    
    def depositar(self,valor:float=0):
        if(not (isinstance(valor,int) or isinstance(valor,float))):
            return;
        valor = float(valor - self.custo_deposito);
        if valor > 0:
            print(f"Valor {round(valor,2)} depositado com sucesso")
            valor += self.saldo;
            self._saldo = valor;
            return 
        print(( "Deposito não efetuado, pois valor do deposito "
                "é menor ou igual o custo de deposito na conta"));
    
    def sacar(self, valor:float=0):
        if(not (isinstance(valor,int) or isinstance(valor,float))):
            return;
        saldo = float(self.saldo + self.limite);
        custo = float(self.custo_saque + valor);
        if saldo >= custo:
            self._saldo = saldo-custo;
            return;
        print(( "Saque não efetuado, pois valor do saldo "
                "é menor que o saque solicitado\n"));
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    pass;
#-----------------------  