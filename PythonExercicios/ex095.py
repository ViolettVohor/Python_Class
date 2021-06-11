jogadores = []
while True:
    print('-'*30)
    jogador = {'Nome': input('Nome do jogador: '),
               'Gols': list(),
               'Total': 0}

    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Partidas'] = partidas
    print('Quantos gols ele fez na...')
    for c in range(0, partidas):
        jogador['Gols'].append(int(input(f'{c + 1}° partida: ')))
        jogador['Total'] += jogador['Gols'][c]

    jogadores.append(jogador.copy())
    jogador.clear()

    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

print('-='*30)
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<6}')
print('-'*60)
for cod, jog in enumerate(jogadores):
    print(f'{cod:>3} {jog["Nome"]:<15} {jog["Gols"]} {jog["Total"]:^6}')

while True:
    while True:
        print('-' * 60)
        esc = int(input('Mostrar dados de qual jogador? '))
        if esc < len(jogadores) or esc == 999:
            break
        else:
            print(f'ERRO! O jogador {esc} não foi cadastrado')

    if esc == 999:
        break

    print(f'LEVANTAMENTO DO JOGADOR {jogadores[esc]["Nome"].upper()}:')
    print(f'    O jogador {jogadores[esc]["Nome"]} jogou {jogadores[esc]["Partidas"]} partidas')
    for p, g in enumerate(jogadores[esc]['Gols']):
        print(f'    => Na partida {p}, fez {g} gols')
    print(f'Foi um total de {jogadores[esc]["Total"]}')

print('<<< VOLTE SEMPRE >>>')
