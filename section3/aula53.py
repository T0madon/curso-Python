"""
Enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)

# for item in enumerate(lista):
#     i, nome = item
#     print(i, nome)

# OU

for i,nome in enumerate(lista):
    print(i, nome)