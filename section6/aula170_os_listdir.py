# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('\\Users', 'joaod', 'OneDrive', 'Documentos', 'Curso Python', 'section6')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo):
        continue

    for item in os.listdir(caminho_completo):
        print('     ', item)