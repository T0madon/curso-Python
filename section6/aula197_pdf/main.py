# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from PyPDF2 import PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20250117.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for i, page in enumerate(reader.pages):
#     print(f'Página {i+1}:\n{page}\n')

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# print(len(page0.images))

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# A seguinte linha coloca todas as pg de um pdf em outro novo

# writer = PdfWriter()
# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf'
]

merger = PdfMerger()
for file in files:
    merger.append(file) # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf') # type: ignore
merger.close() #type:ignore