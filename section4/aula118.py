# Problema dos parâmetros mutáveis em funções Python

def add_cliente(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

cliente1 = add_cliente('Luiz')
add_cliente('Joana', cliente1)
add_cliente('Adriana', cliente1)
print(cliente1)

cliente2 = add_cliente('João')
add_cliente('Vitor', cliente2)
add_cliente('Mara', cliente2)
print(cliente2)
