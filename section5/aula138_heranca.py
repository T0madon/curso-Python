# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '12345'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_classe(self):
        print('Estou na PESSOA')        
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):

    def falar_classe(self):
        print('Estou no CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'

c1 = Cliente('Celso', 'Da Silva')
c1.falar_classe()

a1 = Aluno('João', 'Tomadão')
a1.falar_classe()

print(a1.cpf)