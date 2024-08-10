# dir, hasattr e getattr 

string = 'T0madon'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método ', metodo)