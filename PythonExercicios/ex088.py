from random import randint
from time import sleep

print('-'*40)
print(f'{"Jogue na Mega Sena":^40}')
print('-'*40)

# noinspection SpellCheckingInspection
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*6 + f' Sorteando {quant} jogos ' + '-='*6)

sorteio = []
jogo = []
for index in range (0, quant):  # Faz um loop com a quantidade de jogos que o usuário deseja
    for i in range(0, 6):  # Faz um loop para gerar 6 números aleatórios que não se repetem
        while True:
            num = randint(0, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()  # Organiza os números

    sleep(0.5)
    sorteio.append(jogo[:])
    print(f'Jogo {index+1}: {sorteio[index]}')  # Mostra os palpites
    jogo.clear()
print('-='*7 + ' < Boa sorte! > ' + '-='*7)
