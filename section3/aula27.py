"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
fatiamento [i:f:p] [::]
"""
variavel = 'Olá mundo'
cripto = len(variavel) * '*'
# print(variavel[4])
# print(variavel[-5])
# print(variavel[:5])
# print(len(variavel))
# print(variavel[::-1])
print(cripto)
print(variavel)

cripto = f'{cripto[:1]}l{cripto[2:]}'
print(cripto)