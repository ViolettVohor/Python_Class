cont_man = cont_maior = cont_woman = idade = 0

while True:
    print('-'*30 + f'\n{"CADASTRE UM PESSOA":^30}\n' + '-'*30)

    idade = int(input('Digite a idade da pessoa: '))

    sexo = ''
    while sexo == '':  # Enquanto sexo = '' repete o loop
        # Não tão eficiente, seguir exemplo do ex070
        sexo = input('Digite o sexo da pessoa: ').upper().strip()[0]
        if sexo not in 'FfMm':  # Se sexo não tiver F, f, M ou m
            sexo = ''

    print('='*20)
    while True:  # Enquanto seguir = '' repete o loop
        # Não tão eficiente, seguir exemplo do ex070
        seguir = input('Continuar? [S/N] ').strip()[0]
        if seguir in 'SsNn':  # Se seguir diferente de S e N
            break
    print('='*20)

    if idade > 17:  # Se a pessoa for de maior
        cont_maior += 1  # cont_maior recebe mais 1
    if sexo == 'M':  # Se a pessoa for um homem
        cont_man += 1  # cont_man recebe mais 1
    if sexo == 'F' and idade < 20:  # Se a pessoa for uma mulher e tiver menos que 20 anos
        cont_woman += 1  # cont_woman recebe mais 1

    if seguir in 'nN':  # Se seguir igual n ou N, encerra o laço
        break

print(f'''{cont_maior} pessoas são maiores de idade.
{cont_man} homens foram cadastrados.
{cont_woman} mulheres são menores de 20 anos.''')
