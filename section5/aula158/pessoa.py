from conta import Conta, ContaCorrente, ContaPoupanca

class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name
    
    @property
    def age(self):
        return self.age
    
class Cliente(Pessoa):
    def __init__(self, name, age, cc:  = None, cp = None):
        super().__init__(name, age)
        self.cc = cc
        self.cp = cp

    