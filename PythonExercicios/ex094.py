pessoas = list()
soma = 0
while True:
    pes = {'Nome': input('Nome: '),
           'Sexo': input('Sexo [M/F]: ').strip().upper()[0],
           'Idade': int(input('Idade: '))}
    soma += pes['Idade']
    pessoas.append(pes.copy())
    pes.clear()
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

media = soma / len(pessoas)
print('-='*30)
print(f'- Foram cadastradas {len(pessoas)} pessoas')
print(f'- A média das idades é {media}')
print('- As mulheres cadastradas foram: ', end='')
for pes in pessoas:
    for v in pes.values():
        if v == 'F':
            print(pes['Nome'], end=' ')

print('\n- Lista das pessoas que estão acima da média de idade:\n')
for pes in pessoas:
    for k, v in pes.items():
        if pes['Idade'] > media:
            print(f'{k} = {v};', end=' ')
    if pes['Idade'] > media:
        print('\n')
print('<<< Encerrado >>>')
