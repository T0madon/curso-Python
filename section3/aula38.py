qdd_linhas = 5
qdd_colunas = 5

linha = 1

while linha <= qdd_linhas:
    coluna = 1
    while coluna <= qdd_colunas:
        print(f'{linha=} {coluna=}')
        coluna+=1
    linha+=1
    
print('Acabou')