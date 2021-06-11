jogador = {'Nome': input('Nome do jogador: '),
           'Gols': list(),
           'Total': 0}
partidas = int(input('Quantas partidas ele jogou? '))

print('Quantos gols ele fez na...')
for c in range(0, partidas):
    jogador['Gols'].append(int(input(f'{c+1}° partida: ')))
    jogador['Total'] += jogador['Gols'][c]

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for p, g in enumerate(jogador['Gols']):
    print(f'    => Na partida {p}, fez {g} gols')
print(f'Foi um total de {jogador["Total"]}')
