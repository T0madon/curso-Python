# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    res = 1
    for num in args:
        res *= num
    return res

print(multiplica(1,2,3,4,5))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    return x % 2 == 0

print(par_impar(5))