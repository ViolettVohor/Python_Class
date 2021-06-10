dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    # cont += 1
    if len(pessoas) == 1:  # cont == 1:
        # Caso seja o primeiro valor introduzido na lista pessoas o maior e o menor recebem o mesmo peso
        menor = maior = dados[1]
    else:
        if dados[1] > maior:  # Verifica se o peso inserido é maior que o anterior
            maior = dados[1]
        elif dados[1] < menor:  # Verifica se o peso inserido é maior que o anterior
            menor = dados[1]

    dados.clear()  # Excluí os dados da lista para que eles não se repitam na lista pessoas
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':  # Verifica se o usuário deseja continuar
            break
    if resp in 'N':
        break

print('-='*20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.1f}Kg. Peso de', end=' ')
for p in pessoas:  # Mostra as pessoas que tem o maior peso
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi {menor:.1f}Kg. Peso de', end=' ')
for p in pessoas:  # Mostra as pessoas que tem o menor peso
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
