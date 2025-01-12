from conta import ContaCorrente, ContaPoupanca

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
        return self.age
    
    @age.setter
    def age(self, value: int):
        self._age = value
    
class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account = []

    def add_cc(self, cc: ContaCorrente):
        self.account[0] = cc 

    def add_cp(self, cp: ContaPoupanca):
        self.account[1] = cp 


    