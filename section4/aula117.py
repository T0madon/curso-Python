import json
#caminho_arquivo = '.\\section4\\aula116.txt'

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R5', 'numero': 133},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w+', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         indent=2,
#         )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['enderecos']) #[{'rua': 'R1', 'numero': 32}, {'rua': 'R5', 'numero': 133}]
    for endereco in pessoa['enderecos']:
        print(endereco['rua'])