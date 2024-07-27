primeiro = input('Insira o primeiro valor: ')
segundo = input('Insira o segundo valor: ')

if primeiro > segundo:
    print(f'{primeiro=} é maior do que {segundo=}')
elif segundo > primeiro:
    print(f'{segundo=} é maior do que {primeiro=}')
elif primeiro==segundo:
    print(f'{segundo=} é igual ao {primeiro=}')
else:
    print('Os valor não podem ser comparados!')