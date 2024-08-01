"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém um chave
pop - Apaga um item com a chave especificada(del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro 
"""
pessoa = {
    'nome': 'João Vitor',
    'sobrenome': 'T0madon Daciuk',
    'idade': 900,
}

# print('Tamanho', len(pessoa))
# print('Keys' ,list(pessoa.keys()))
# print('Values',list(pessoa.values()))
# print('items', list(pessoa.items()))
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

print('\nPARTE 2\n')

#  Exemplo de uso
# for item in pessoa:
#     print(item)

# for chave, valor in pessoa.items():
#     print(chave + ' : ' + valor)

p1 = {
    'nome': 'Tomate',
    'sobrenome': 'da sal',
}

print(p1.get('nome'))

# nome = p1.pop('nome')
# print(f'{nome} foi excluído\n{p1}')

# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30 
})

print(p1)