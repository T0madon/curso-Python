frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum.'.lower()

i=0
qdd_mais_aparece = 0

while i<len(frase):
    letra_atual = frase[i]
    print(frase[i], frase.count(letra_atual))
    if letra_atual != ' ':
        qdd_letra_atual = frase.count(letra_atual)

        if(qdd_letra_atual > qdd_mais_aparece):
            qdd_mais_aparece = qdd_letra_atual
            letra = letra_atual

    i+=1    

print(f'\nA letra que mais aparece é a letra {letra}, aparecendo {qdd_mais_aparece} vezes')