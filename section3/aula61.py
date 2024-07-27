"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
""" 

while True:
    user_cpf = input('Insira seu CPF no formato (123.456.789-00): ').replace('.','',2).replace('-','')
    num_1 = user_cpf[12]
    num_2 = user_cpf[13]    
    cpf_contas_1 = user_cpf[:-2]
    cpf_contas_2 = user_cpf[:-1]

    soma = 0
    multiplicador = 10

    for num in cpf_contas_1:
        soma += (int(num) * multiplicador)
        multiplicador -= 1
    
    confere = (soma*10)% 11

    primeiro_digito = confere if confere <= 9 else 0

    soma = 0
    multiplicador = 11

    for num in cpf_contas_2:
        soma += (int(num) * multiplicador)
        multiplicador -= 1
    
    confere = (soma*10)% 11

    segundo_digito = confere if confere <= 9 else 0
    



    