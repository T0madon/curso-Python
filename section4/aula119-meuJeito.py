import os
import copy
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
x=1

todo = []
lista_refazer = []

def listar(tarefas):
    print("\nTAREFAS:")
    for tarefa in tarefas:
        print(tarefa)

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print("\nNão há tarefas para desfazer!")
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print("\nNão há tarefas para refazer!")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adiciona(item, lista):
    item = item.strip()
    if not item:
        print("\nVocê não digitou nada!")
        return
    lista.append(item)

while(True):
    print('\nComandos: listar, desfazer, refazer, cls, exit')
    comando = input("Digite uma tarefa ou comando: ")
    
    if comando == "listar":
        listar(todo)
    
    elif comando == "desfazer":
        desfazer(todo, lista_refazer)
        listar(todo)

    elif comando == "refazer":
        refazer(todo, lista_refazer)
        listar(todo)

    elif comando == "cls":
        os.system("cls")

    else:
        adiciona(comando, todo)
        

    
    