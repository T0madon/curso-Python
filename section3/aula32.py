"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print(10*'-' + 'EXERCÍCIO 1' + 10*'-')
num = input('Digite um número inteiro: ')

try:
    hora_int = int(num)
    if hora_int % 2 == 0:
        print('Seu número é par!')
    else:
        print('Seu número é ímpar!')
except:
    print('O caracter inserido não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('\n' + 10*'-' + 'EXERCÍCIO 2' + 10*'-')
hora = input('Insira o horário atual: ')

try:
    hora_int = int(hora)

    dia = hora_int >= 0 and hora_int <= 11
    tarde = hora_int >= 12 and hora_int <= 17
    noite = hora_int >= 18 and hora_int <= 23

    if dia:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite!')
    else:
        print('Digite um valor inteiro no intervalo [0;23]')
except:
    print('O caracter inserido não é um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('\n'+10*'-' + 'EXERCÍCIO 3' + 10*'-')
nome = input('Insira seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')