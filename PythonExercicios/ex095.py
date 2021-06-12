jogadores = []
while True:
    print('-'*30)
    jogadora = {'Nome': input('Nome do(a) jogador(a): '),
               'Gols': list(),
               'Total': 0}

    partidas = int(input(f'Quantas partidas {jogadora["Nome"]} jogou? '))
    jogadora['Partidas'] = partidas
    print('Quantos gols ele(a) fez na...')
    for c in range(0, partidas):  # Armazena a quantidade de gols em cada partida
        jogadora['Gols'].append(int(input(f'{c + 1}° partida: ')))
        jogadora['Total'] += jogadora['Gols'][c]  # E calcula o total

    jogadores.append(jogadora.copy())  # Adiciona o dicionário a lista jogadores
    jogadora.clear()

    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas "N" ou "S"')
    if resp in 'N':
        break

print('-='*30)
print(f'COD {"NOME":<15} {"GOLS":<15} {"TOTAL":<6}')
print('-'*60)
for cod, jog in enumerate(jogadores):  # Tabela dos(as) Jogadores(as)
    print(f'{cod:>3} {jog["Nome"]:<15} {str(jog["Gols"]):<15} {jog["Total"]:<6}')

while True:
    while True:
        print('-' * 60)
        esc = int(input('Mostrar dados de qual jogador(a)? '))
        # Caso a escolha esteja dentro dos códigos das(os) Jogadoras(es) ou seja igual a 999
        if -1 < esc < len(jogadores) or esc == 999:
            break
        print(f'ERRO! O jogador(a) {esc} não foi cadastrado')

    if esc == 999:
        break

    # Mostra os Dados das(os) Jogadoras(es)
    print(f'LEVANTAMENTO DO JOGADOR(A) {jogadores[esc]["Nome"].upper()}:')
    print(f'    O(A) jogador(a) {jogadores[esc]["Nome"]} jogou {jogadores[esc]["Partidas"]} partidas')
    for p, g in enumerate(jogadores[esc]['Gols']):
        print(f'    => Na partida {p}, fez {g} gols')
    print(f'Foi um total de {jogadores[esc]["Total"]}')

print('<<< VOLTE SEMPRE >>>')
