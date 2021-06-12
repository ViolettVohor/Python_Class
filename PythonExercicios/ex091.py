from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados:')
# Sorteia os 4 dados para os 4 jogadores
jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
for k, v in jogos.items():  # Mostra os dados de cada jogador
    print(f'    O {k} tirou {v}')
    sleep(0.5)

print('Ranking dos Jogadores:')
'''jogadores = list()  # Lista de controle
for i in range(0, 4):  # Organiza os jogadores dos que tem o maior dado até o menor
    maior = 0
    kmaior = ''
    for k, v in jogos.items():  # Percorre o dicionário com os jogadores
        if k not in jogadores:  # Se o jogador não tiver sido reordenado, estive fora da lista de controle
            if v > maior:  # Verifica se o dado dele é o maior
                maior = v
                kmaior = k
    del jogos[kmaior]  # Deleta o jogador que foi tiver o maior dado e não estiver na lista de controle
    jogos[kmaior] = maior  # Adiciona o jogador, que foi tinha o maior dado nesse loop, no final do dicionário
    jogadores.append(kmaior)  # Adiciona a chave do jogador a lista de controle'''

jogo = sorted(jogos.items(), key=itemgetter(1), reverse=True)  # Organiza o dicionário
# assim como o trecho comentado acima
for i, v in enumerate(jogo):  # Mostra os jogadores em ranking
    print(f'    {i+1}° lugar: {v[0]} tirou {v[1]}')
    sleep(0.5)
