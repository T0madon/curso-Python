# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,
    metavar='STRING',
    # default='Olá mundo',
    action='append', # Recebe o argumento mais de uma vez
    # nargs='+', Recebe mais de um valor
    )
args = parser.parse_args()

if args.basic is None:
    print('Você não passou argumentos para o valor de b.')
    print(args.basic)
else:
    print(args.basic)
