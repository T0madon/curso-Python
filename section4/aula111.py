from functools import partial

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

# novos_produtos = [
#     {**p, 'preco': p['preco']*2} for p in produtos 
# ]
# UTILIZANDO MAP

def muda_preco(prod):
    return {**prod, 'preco': prod['preco']*2} 

novos_produtos = map(muda_preco, produtos)

# print_iter(novos_produtos)

print(
    list(map(
        lambda x: x*2,
        [1,2,3,4]
    ))
)