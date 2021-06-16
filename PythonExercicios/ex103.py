def ficha(nome='<desconhecido>', gols=0):
    print(f'O(A) jogador(a) {nome} fez {gols} gol(s) no campeonato.')


jog = input('Nome do(a) jogador(a): ')
gol = input('Número de Gols: ')

if jog != '' and gol != '':
    ficha(jog, int(gol))
elif jog == '' and gol == '':
    ficha()
elif jog == '' and gol != '':
    ficha(gols=int(gol))
elif jog != '' and gol == '':
    ficha(jog)
