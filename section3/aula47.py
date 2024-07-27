"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os


palavra = 'termo'
acertou = False
num_tentativa = 0
criptografada = len(palavra) * '*'

while not acertou:

    tentativa = input('Digite uma letra: ')
    if len(tentativa) == 1:
        i=0
        num_tentativa+=1
        for letra in palavra:
            if tentativa == letra:
                criptografada = f'{criptografada[:i]}{letra}{criptografada[i+1:]}'
            i+=1

        if(criptografada == palavra):
            os.system('cls')
            print('VOCÊ GANHOU!! PARABÉNS\n' \
                 f'A palavra era: {palavra}\n' \
                 f'Tentativas: {num_tentativa}')
            acertou = True
        else:
            print(f'Palavra formada: {criptografada}')
    else:
        print('Digite APENAS uma letra !')
    

print('\nPrograma encerrado!')