from itertools import zip_longest

def soma_lista(l1,l2):
    indice = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(indice)
    ]

la = [1,2,3,4,5,6,7]
lb = [1,2,3,4]

print(soma_lista(la,lb))
# OUUUU
res = [x + y for x,y in zip(la,lb)]
print(res)

print(list(zip(la,lb)))

# ou para juntar as 2 listas independente dos tamanhos

lista_final = [x + y for x,y in zip_longest(la,lb,fillvalue=0)]
print(lista_final)
