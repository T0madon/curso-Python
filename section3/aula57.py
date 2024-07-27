salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])

# for sala in salas:
#     for aluno in sala:

for i in range(len(salas)):
    for j in range(i):
        print(salas[i][j])