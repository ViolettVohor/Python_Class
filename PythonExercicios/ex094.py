pessoas = list()
soma = 0
while True:
    pes = {'Nome': input('Nome: ')}  # Dicionário com os dados da pessoas
    while True:
        pes['Sexo'] = input('Sexo [F/M]: ').strip().upper()[0]
        if pes['Sexo'] in 'FM':
            break
        print('ERRO! Responda "F" ou "M"')
    pes['Idade'] = int(input('Idade: '))

    soma += pes['Idade']  # Soma da idade que será usada para a média
    pessoas.append(pes.copy())  # lista pessoas recebe uma cópia do dicionário pes

    while True:
        resp = input('Deseja continuar? [N/S]: ').strip().upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda "N" ou "S"')
    if resp in 'N':
        break

media = soma / len(pessoas)
print('-='*30)
print(f'- Foram cadastradas {len(pessoas)} pessoas')
print(f'- A média das idades é {media:5.2f}')

print('- As mulheres cadastradas foram: ', end='')
for pes in pessoas:  # Mostra o nome das mulheres
    if pes['Sexo'] == 'F':
       print(pes['Nome'], end=' ')

print('\n- Lista das pessoas que estão acima da média de idade:\n')
for pes in pessoas:  # Mostra as pessoa que são mais velhas que a média
    for k, v in pes.items():
        if pes['Idade'] > media:
            print(f'{k} = {v};', end=' ')
    if pes['Idade'] > media:
        print('\n')
print('<<< Encerrado >>>')
