jogador = {'Nome': input('Nome do jogador: '),
           'Gols': list(),
           'Total': 0}
partidas = int(input(f'Quantas partidas o(a) jogador(a) {jogador["Nome"]} jogou? '))

print('Quantos gols ele fez na...')
for c in range(0, partidas):  # Recebe a quantidade de gols para cada partida
    jogador['Gols'].append(int(input(f'{c+1}° partida: ')))
    # jogador['Total'] += jogador['Gols'][c]
jogador['Total'] = sum(jogador['Gols'])  # Faz a soma de todos os gols do campeonato

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():  # Mostra os dados no dicionário
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for p, g in enumerate(jogador['Gols']): # Mostra os gols para cada partida
    print(f'    => Na partida {p}, fez {g} gols')
print(f'Foi um total de {jogador["Total"]}')
