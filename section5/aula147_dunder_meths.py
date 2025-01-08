# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto():
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        # classname = self.__class__.__name__ OU
        classname = type(self).__name__
        
        return f'{classname}(x={self.x!r}, y={self.y!r}, z={self.z!r})' 
        # Nesse caso, sem a !r, o retorno é String, com !r é 'String'

p1 = Ponto(1,2)
p2 = Ponto(978, 897)

print(p1)
# Outra forma pra ver o repr
print(repr(p2))
# ou
print(f'{p2!r}')
