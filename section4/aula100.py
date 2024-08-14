import copy
from dados import produtos
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


novos_produtos = [
    {**prod, 'preco': round(prod['preco'] * 1.1, 2)}
    for prod in copy.deepcopy(produtos)     
]

print(*novos_produtos, sep='\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True
    )
    
# print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(
    sorted(produtos, key=lambda p: p['preco'])
)
# print(*produtos_ordenados_por_preco, sep='\n')
