# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print('Abrindo')
        arquivo = open(caminho, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro:', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\nLinha 2\nLinha 3')
    print('WITH', arquivo)