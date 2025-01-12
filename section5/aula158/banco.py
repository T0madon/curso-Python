from pessoa import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

class Banco:
    def __init__(self, bank: str) -> None:
        self.bank = bank
        self._users = [] # Cliente
        self._accounts = [] # Conta
        self._agencies = [] #

    def add_user(self, user) -> None:
        self._users.append(user)
    
    def show_users(self) -> None:
        print(f'Usuários {type(self).__name__}:')
        for user in self._users:
            print(f'({user.name}, {user.age})')

    def add(self, attr):
        clas = type(attr).__name__

        if clas == 'Cliente':
            self._users.append(attr)
            return
        if (clas == 'ContaCorrente') | (clas == 'ContaPoupanca'):
            self._accounts.append(attr)
            return
        self._agencies.append(attr)

    def show(self, attr):
        clas = type(attr).__name__
        

if __name__ == '__main__':

    bb = Banco('Banco do Brasil')
    c1 = Cliente('João', 20)
    cc1 = ContaCorrente(123, 321, 1000, 10)

    bb.add(c1)





