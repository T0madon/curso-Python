# Variáveis livres + nonlocal (locals, globals)
# def fora(x):
#     a = x

#     def dentro():
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concat(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concat=''):
        nonlocal valor_final
        valor_final += valor_a_concat
        return valor_final
    return interna

c = concat('a')
print(c('b'))
print(c('c'))
print(c('d'))