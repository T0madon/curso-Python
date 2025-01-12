from conta import ContaCorrente, ContaPoupanca, Conta

class Pessoa:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value: int):
        self._age = value

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'
    
class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: Conta | None = None

if __name__ == '__main__':
    c1 = Cliente('João', 30)
    c1.account = ContaCorrente(123, 321, 100, 1000)

    print(c1)
    print(c1.account)

    