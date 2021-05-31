cont_man = cont_maior = cont_woman = idade = 0

while True:
    sexo = seguir = ''
    print('-'*30 + f'\n{"CADASTRE UM PESSOA":^30}\n' + '-'*30)
    idade = int(input('Digite a idade da pessoa: '))
    while sexo == '':
        sexo = input('Digite o sexo da pessoa: ').split()[0]
        if sexo not in 'FfMm':
            sexo = ''

    print('='*20)
    while seguir == '':
        seguir = input('Continuar? [S/N] ').upper().split()[0]
        if seguir != 'S' and seguir != 'N':
            seguir = ''
    print('='*20)

    if idade > 17:
        cont_maior += 1
    if sexo in 'M':
        cont_man += 1
    if sexo == 'F' and idade < 20:
        cont_woman += 1

    if seguir in 'nN':
        break
print(f'''{cont_maior} pessoas são maiores de idade.
{cont_man} homens foram cadastrados.
{cont_woman} mulheres são menores de 20 anos.''')
