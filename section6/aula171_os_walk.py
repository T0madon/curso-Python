# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os

count = 0
caminho = os.path.join('\\Users', 'joaod', 'OneDrive', 'Documentos', 'Curso Python', 'section6')

for root, dirs, files in os.walk(caminho):
    print(count,'Pasta atual', root)
    count+=1

    for dir_ in dirs:
        print('     ', count, 'Dir', dir_)
        
    for file_ in files:
        print('     ', count, 'FILE', file_)
