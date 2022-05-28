# 🐍 Desafio POO

## Esse programa tem como intuito de reforçar o meu conhecimento em POO em python.

```
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco.A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanças)
Criar classes ContaPoupanças e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    - Checar se a agência é daquele banco
    - Checar se o cliente é daquele banco
    - Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
```
