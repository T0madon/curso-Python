# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple

@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome) -> None:
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    lista = [ Pessoa('B', 'C'), Pessoa('A', 'Z'), Pessoa('C', 'A')]
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.nome)
    print(ordenadas)
    print()
    p1 = Pessoa('João', 'T0madon')
    print(asdict(p1))
    print(astuple(p1))
