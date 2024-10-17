# filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_prod = [
#     p for p in produtos
#     if p['preco'] >= 20
# ]
# OOOU

def filtrar_prod(prod):
    return prod['preco'] >= 20

novos_prod = filter(
    # lambda p: p['preco'] >= 20,
    filtrar_prod,
    produtos
)

print_iter(novos_prod)
# print_iter(produtos)