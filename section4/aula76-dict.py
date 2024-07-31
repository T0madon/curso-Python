pessoa = {
    'nome': 'João Vitor',
    'sobrenome': 'T0madon Daciuk',
    'idade': 19,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'Av. Brasil', 'número': 2019},
        {'rua': 'Balduíno', 'número': 157},
    ],
}

print(pessoa['enderecos'])
print(pessoa['enderecos'][0]['rua'])

print(pessoa.get('chavequenaoexiste'))

if pessoa.get('chave') is not None:
    print('Existe')
else:
    print('Não existe')