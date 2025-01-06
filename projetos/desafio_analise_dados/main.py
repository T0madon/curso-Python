import pandas as pd

# Carregar o dataset caminho_arquivo = '.\\section4\\aula116.txt'
file_path = 'C:\\Users\\joaod\\OneDrive\\Documentos\\Curso Python\\projetos\\desafio_analise_dados\\Dataset.csv'
data = pd.read_csv(file_path)

# Visualizar as primeiras linhas do dataset
data.head()
