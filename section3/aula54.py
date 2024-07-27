"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    acao = input('[i]nserir  [a]pagar  [l]istar: ').lower()

    if acao == 'l':
        os.system('cls')
        if not lista:
            print('Nada para listar!')
        else:
            for i,item in enumerate(lista):
                print(i, item)
    
    elif acao == 'i':
        os.system('cls')
        new_item = input('O que deseja inserir ? ')
        lista.append(new_item)

    elif acao == 'a':
        os.system('cls')
        try:
            remove_item = int(input('Escolha o índice para apagar: '))
            if(remove_item in range(len(lista))):
                print(f'{lista[remove_item]} removido com sucesso')
                del lista[remove_item]
            else:
                print('Índice não pertence à lista')
        except:
            print('Não foi possível apagar esse índice')
        
    
    else:
        print('Ação inválida, tente novamente !')
            


