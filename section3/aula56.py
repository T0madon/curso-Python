"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Olha só, que coisa interessante'
lista_frases= frase.split(',')

lista_frases_new = []

for i, frase in enumerate(lista_frases):
    lista_frases_new.append(lista_frases[i].strip())

print(lista_frases)

frases_unidas = '-'.join(lista_frases_new)

print(frases_unidas)

