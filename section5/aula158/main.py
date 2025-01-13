from bancos import Banco
from conta import Conta, ContaCorrente, ContaPoupanca
from pessoa import Cliente
"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa ()
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""


bb = Banco('Banco do Brasil')

# Add agências
bb.add(123)
bb.add(432)

# Clientes
c1 = Cliente('João', 20)
c2 = Cliente('Pedro', 19)
c3 = Cliente('Sara', 34)
 
# Contas
cc1 = ContaCorrente(123, 321, 1000, 10)
cp2 = ContaPoupanca(432, 100, 500)
cc3 = ContaCorrente(124, 547, 700, 500)

# Add clientes e mostrando
bb.add(c1)
bb.add(c2)
bb.add(c3)
# bb.show_users()

# Add contas e mostrando
bb.add(cc1)
bb.add(cp2)
bb.add(cc3)
bb.show_accounts()