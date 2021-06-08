from random import randint
from time import sleep

print('-'*40)
print(f'{"Jogue na Mega Sena":^40}')
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*6 + f' Sorteando {jogos} jogos ' + '-='*6)

sorteio = []
jogo = []
for index in range (0, jogos):
    for i in range(0, 6):
        while True:
            num = randint(0, 60)
            if num not in jogo:
                jogo.append(num)
                jogo.sort()
                break
    sleep(0.5)
    sorteio.append(jogo[:])
    print(f'Jogo {index+1}: {sorteio[index]}')
    jogo.clear()
print('-='*7 + ' < Boa sorte! > ' + '-='*7)
