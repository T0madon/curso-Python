perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1', '2', '4', '10'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '10', '15', '48'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['2', '5', '0', '20'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}\n\nOpções:')
    for i,option in enumerate(pergunta['Opções']):
        print(f'{i}) {option}') 
    try:
        i_user_answer = int(input('Escola uma opção: '))
        f_user_answer = pergunta['Opções'][i_user_answer]
        if f_user_answer == pergunta['Resposta']:
            print('Acertou! Parabéns!!\n')
        else:
            print('Errooooooou!! ZERO!!\n')
    except:
        print('Errooooooou!! ZERO!!\n')

