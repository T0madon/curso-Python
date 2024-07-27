while True:
    num1 = input('Insira um valor: ')
    op = input('Insira o operador(-, +, *, /): ')
    num2 = input(f'Insira o segundo valor: {num1} {op} ')

    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '-':
            res = num1 - num2
            print(f'{num1} - {num2} = {res}')
        elif op == '+':
            res = num1 + num2
            print(f'{num1} + {num2} = {res}')
        elif op == '*':
            res = num1 * num2
            print(f'{num1} * {num2} = {res}')
        elif op == '/':
            res = num1 / num2
            print(f'{num1} / {num2} = {res}')
        else:
            print(f'O operador {op} não é válido!')
        
    except:
        print('Valores inseridos inválidos!')


    sair = input('Deseja [s]air? ').lower().startswith('s')
    if sair:
        break
    print(10*'-')

print("Obrigado por utilizar T0madon's calculator")