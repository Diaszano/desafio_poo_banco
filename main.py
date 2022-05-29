"""Main"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from banco   import Banco
from cliente import Cliente
from conta   import ContaCorrente,ContaPoupanca
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------  
if(__name__ == "__main__"):
    banco = Banco();
    cliente1 = Cliente('Luiz', '22/01/1995');
    cliente2 = Cliente('Maria', '2/06/2002');
    cliente3 = Cliente('João', '15/10/1983');

    conta1 = ContaPoupanca(agencia=1,saldo=254136);
    conta2 = ContaCorrente(agencia=2,saldo=254137,limite=550);
    conta3 = ContaPoupanca(agencia=1,saldo=254138);

    cliente1.adicionar_conta(conta1);
    cliente2.adicionar_conta(conta2);
    cliente3.adicionar_conta(conta3);

    banco.adicionar_contas(cliente2);
    banco.adicionar_contas(conta2);

    banco.adicionar_cliente(cliente1);
    banco.adicionar_contas(conta1);

    banco.adicionar_cliente(cliente3);
    banco.adicionar_contas(conta3);

    print('#'*55);
    
    if banco.autenticar(cliente1):
        cliente1.contas.depositar(0);
        cliente1.contas.sacar(20);
    else:
        print('Cliente não autenticado.');

    print('#'*55);

    if banco.autenticar(cliente2):
        cliente2.contas.sacar(0);
        cliente2.contas.sacar(20);
    else:
        print('Cliente não autenticado.');
    
    print('#'*55);
    
    if banco.autenticar(cliente3):
        cliente3.contas.sacar(0);
        cliente3.contas.sacar(20);
    else:
        print('Cliente não autenticado.');

    print('#'*55);
#----------------------- 