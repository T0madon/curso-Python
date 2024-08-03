#Exemplo de uso - Set
letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('A letra "l" ou "L" sai do programa!')
        break

    print(letras)