def ficha(nome='<desconhecido>', gols=0):
    """
    -> Mostra o nome do(a) jogador(a) e seus gols
    :param nome: nome do(a) jogador(a) (padrão <desconhecido>)
    :param gols: quantidade de gols (padrão 0)
    :return: sem retorno
    """
    print(f'O(A) jogador(a) {nome} fez {gols} gol(s) no campeonato.')


jog = input('Nome do(a) jogador(a): ').strip()
gol = input('Número de Gols: ')

if gol.isnumeric():  # Caso gol for númerico, é convertido em inteiro
    gol = int(gol)
else:  # Caso não recebe o valor
    gol = 0

if jog != '':  # Caso o nome do jogador tiver sido preenchido, ele é informado na chamada
    ficha(jog, gol)
elif jog == '':  # Caso não ele não é informado e é utilizado o valor padrão
    ficha(gols=gol)
