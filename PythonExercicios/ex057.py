sexo = ' '
verd = True
while verd:
    sexo = input('Digite o seu sexo [M/F]: ').upper()
    if sexo == 'M' or sexo == 'F':
        verd = False
    else:
        print('Digite um valor valido')
print(f'Seu sexo é {sexo}')
