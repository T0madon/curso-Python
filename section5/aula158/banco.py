from pessoa import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

class Banco:
    def __init__(self, bank: str) -> None:
        self.bank = bank
        self._users = [] # Cliente
        self._accounts = [] # Conta
        self._agencies = [] #

    def check(self):
        ...

    def add(self, attr):
        clas = type(attr).__name__

        if clas == 'Cliente':
            self._users.append(attr)
            return
        if (clas == 'ContaCorrente') | (clas == 'ContaPoupanca'):
            self._accounts.append(attr)
            return
        self._agencies.append(attr)

    def show_users(self) -> None:
        print(f'Usuários {self.bank}:')
        for user in self._users:
            print(f'({user.name}, {user.age})')

    def show_accounts(self) -> None:
        print(f'Contas existentes:')
        for acc in self._accounts:
            if (type(acc).__name__ == 'ContaPoupanca'):
                print(f'Agência: {acc.agency} # Número: {acc.number} '
                f'  # Saldo {acc.balance}')
            else:
                print(f'Agência: {acc.agency} # Número: {acc.number} '
                f'  # Saldo {acc.balance} # Limite: {acc.lim}')    


if __name__ == '__main__':

    bb = Banco('Banco do Brasil')

    # Add agências
    bb.add(123)
    bb.add(432)
    bb.add(123)

    # Clientes
    c1 = Cliente('João', 20)
    c2 = Cliente('Pedro', 19)
    c3 = Cliente('Sara', 34)

    # Contas
    cc1 = ContaCorrente(123, 321, 1000, 10)
    cp2 = ContaPoupanca(432, 100, 500)
    cc3 = ContaCorrente(123, 547, 700, 500)

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





