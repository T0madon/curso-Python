produto = {
    'nome': 'Jota quest',
    'preco': 25.00,
    'categoria': 'Música',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in produto.items()
}

print(dc)