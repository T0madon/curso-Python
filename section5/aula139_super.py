# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'Valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Ei, burlei o sistema')

    def metodo(self):
        # super(B, self).metodo()
        # super(C, self).metodo() #Colocar super(C,self) é redundante == super()
        # Aqui no super, ele olha a partir de C, qm é o q está acima ?
        A.metodo(self)
        print('C')

c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

#c.metodo()