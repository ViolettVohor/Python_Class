from random import randint
print('Valores sorteados:')
jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
for k, v in jogos.items():
    print(f'    O {k} tirou {v}')

print('Ranking dos Jogadores:')
jogadores = list()
for i in range(0, 4):
    maior = 0
    kmaior = ''
    for k, v in jogos.items():
        if k not in jogadores:
            if v > maior:
                maior = v
                kmaior = k
    del jogos[kmaior]
    jogos[kmaior] = maior
    jogadores.append(kmaior)

cont = 0
for k, v in jogos.items():
    cont += 1
    print(f'    {cont}° lugar: {k} tirou {v}')
