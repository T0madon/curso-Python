# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = caminho = os.path.join(HOME, 'OneDrive', 'Documentos', 'Curso Python', 'section6')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'aula170_pastaTeste')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# shutil.rmtree(NOVA_PASTA) # APAGA
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) # COPIA
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA') # RENOMEIA/MOVE