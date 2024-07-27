# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(acao):
    def calcula(num):
        return num * acao
    return calcula

duplica = multiplicador(2)
triplica = multiplicador(3)
quadriplica = multiplicador(4)
quintuplica = multiplicador(5)

print(duplica(2))
print(triplica(2))
print(quadriplica(2))
print(quintuplica(2))
