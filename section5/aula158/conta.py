from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agency, number, balance):
        self.agency = agency
        self.number = number
        self.balance = balance

    @abstractmethod
    def take(self, value):
        ...

    def deposit(self, value):
        self.balance += value
        self.details(f'(DEPÓSITO DE R${value:.2f})')

    def details(self, msg=''):
        print(f'{msg}\nO seu saldo é de R${self.balance:.2f} ')
        print('-----------')

class ContaCorrente(Conta):
    
    def take(self, value):

        if (self.balance - value) >= 0:
            self.balance -= value
            self.details(f'SAQUE DE R${value:.2f}')
            return
        
        print(f'Não foi possível sacar o valor de R${value}')
        self.details()


class ContaPoupanca(Conta):
    def take(self, value):
        
        if (self.balance - value) >= 0:
            self.balance -= value
            self.details(f'SAQUE DE R${value:.2f}')
            return
        
        print(f'Não foi possível sacar o valor de R${value}')
        self.details()

if __name__ == '__main__':
    cp1 = ContaPoupanca(252, 1, 10)
    cp1.take(9)
    cp1.deposit(2)
    cp1.take(3)
