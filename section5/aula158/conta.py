from abc import ABC, abstractmethod
from section5.aula158.bancos import Banco

class Conta(ABC):
    def __init__(self, agency: int, number: int, balance: float =0) -> None :
        self.agency = agency
        self.number = number
        self.balance = balance

    @abstractmethod
    def take(self, value: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'(DEPÓSITO DE R${value:.2f})')
        return self.balance

    def details(self, msg: str ='') -> None:
        print(f'{msg}\nO seu saldo é de R${self.balance:.2f} ')
        print('-----------')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.number!r}, {self.balance!r})'
        return f'{class_name}{attrs}'

class ContaCorrente(Conta):
    def __init__(self, agency: int, number: int, balance=0, lim=0):
        super().__init__(agency, number, balance)
        self.lim = lim


    def take(self, value):
        if (self.balance - value) >= -self.lim:
            self.balance -= value
            self.details(f'SAQUE DE R${value:.2f}')
            return
        
        print(f'Não foi possível sacar o valor de R${value}')
        self.details()
        return self.balance
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.number!r}, {self.balance!r}, {self.lim!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def take(self, value):

        if (self.balance - value) >= 0:
            self.balance -= value
            self.details(f'SAQUE DE R${value:.2f}')
            return
        
        print(f'Não foi possível sacar o valor de R${value}')
        self.details()

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.take(1)
    cp1.deposit(2)
    cp1.take(1)
    cp1.take(1)
    print('###')
    cc1 = ContaCorrente(523, 123, 0, 100)
    cc1.take(1)
    cc1.deposit(2)
    cc1.take(1)
    cc1.take(1)

 