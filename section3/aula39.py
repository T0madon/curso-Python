nome = 'João Vitor'
tam = len(nome)

# Eu quero que fique assim:
# *J*o*ã*o* *V*i*t*o*r

cont = 0
novo = ''
while cont < tam:
    novo += f'*{nome[cont]}'
    cont+=1

print(novo)
    