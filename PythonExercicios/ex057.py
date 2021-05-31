sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
verd = True
while sexo not in 'MF':
        sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
