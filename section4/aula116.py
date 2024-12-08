caminho_arquivo = 'C:\\Users\\joaod\\OneDrive\\Documentos\\Curso Python\\section4\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')