# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("APAGANDO", self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("APAGANDO", self.rua, self.numero)

        
c1 = Cliente("João")
c1.inserir_endereco('Curitiba', 60)
c1.inserir_endereco('São Paulo', 939)
# c1.listar_enderecos()

end_externo = Endereco('Rua A', 111)
c1.inserir_endereco_externo(end_externo)
c1.listar_enderecos() 

del c1

print(end_externo.rua, end_externo.numero)
print('FIIIIIIIIIIIIIIIIM')