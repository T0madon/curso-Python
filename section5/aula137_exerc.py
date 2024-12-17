# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, modelo, motor, fabricante):
        self.modelo = modelo
        self.motor = motor
        self.fabricante = fabricante
        fabricante.carros.append(self.modelo)

    def mostra_infos(self):
        print(f'INFOS')
        print('Modelo:', self.modelo)
        print('Motor:', self.motor.tipo)        
        print('Fabricante:', self.fabricante.marca)        
    
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Fabricante:
    def __init__(self, marca):
        self.marca = marca
        self.carros = []

    def mostraCarros(self):
        print(f'\n{self.marca} - CARROS FABRICADOS')
        for carro in self.carros:
            print(carro)


f1 = Fabricante('Fiat')
m1 = Motor('1.6')
m2 = Motor('1.0')

carro1 = Carro('Grand Siena', m1, f1)
carro2 = Carro('Mobi', m2, f1)

carro1.mostra_infos()
print()
carro2.mostra_infos()

f1.mostraCarros()




    # GETTERS
    # @property
    # def modelo(self):
    #     return self.modelo
    # @property
    # def motor(self):
    #     return self.motor
    # @property
    # def fabricante(self):
    #     return self.fabricante
    
    # SETTERS
    # @modelo.setter
    # def modelo(self, modelo):
    #     self.modelo = modelo
    # @motor.setter
    # def motor(self, motor):
    #     self.motor = motor
    # @fabricante.setter
    # def fabricante(self, fabricante):
    #     self.fabricante = fabricante