dados = []
pessoas = []
cont = maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])

    cont += 1
    if cont == 1:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    dados.clear()
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

print('-='*20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')

print(f'\nO menor peso foi {menor:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
