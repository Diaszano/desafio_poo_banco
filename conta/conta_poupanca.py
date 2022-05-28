"""Classe das Contas Poupança

    A Classe das Contas poupança é uma classe aonde criaremos as 
    contas poupança dos users.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from .conta import Conta
#-----------------------
# CLASSES
#-----------------------
class ContaPoupanca(Conta): 

    __custo_deposito    : float = 3.75;
    __custo_saque       : float = 4.65;
    
    def __init__(self, agencia: int = 0, saldo: float = 0) -> None:
        super().__init__(agencia, saldo);
    
    def __str__(self):
        mensagem:str = f"Conta: {self.conta} Agência: {self.agencia}\n";
        mensagem    += f"Saldo da conta: R${self.saldo}\n";
        return mensagem;
    
    @property
    def custo_saque(self)->float:
        return self.__custo_saque;
    
    @property
    def custo_deposito(self)->float:
        return self.__custo_deposito;
    
    
    def depositar(self,valor:float=0):
        if(not (isinstance(valor,int) or isinstance(valor,float))):
            return;
        valor = float(valor - self.custo_deposito);
        if valor > 0:
            print(f"Valor {round(valor,2)} depositado com sucesso");
            valor += self.saldo;
            self._saldo = valor;
            return; 
        print(( "Deposito não efetuado, pois valor do deposito "
                "é menor ou igual o custo de deposito na conta"));

    def sacar(self, valor:float=0):
        if(not (isinstance(valor,int) or isinstance(valor,float))):
            return;
        custo = float(self.custo_saque + valor);
        if self.saldo >= custo:
            print(f"Valor {round(valor,2)} sacado com sucesso");
            self._saldo = self._saldo-custo;
            return;
        print(( "Saque não efetuado, pois valor do saldo "
                "é menor que o saque solicitado\n"));

#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    a = ContaPoupanca(22,1500.98158418);
    a.depositar(15.00)
    a.sacar(8000);
    print(a);
#-----------------------  