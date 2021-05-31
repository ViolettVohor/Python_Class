from random import randint
result = True
vitorias = 0

print('-=-'*10 + f'\n{"Vamos Jogar Par ou Ímpar":^30}')

while True:
    player = str(input('-=-'*10 + '\nÍmpar ou Par? ')).upper().split()[0]

    if not player in 'IÍP':
        print('\nDigite Ímpar ou Par.\n')
        continue

    pc_num = randint(0, 10)
    player_num = int(input('Digite um número entre 0 e 10: '))

    soma = pc_num + player_num

    print('-'*20 + f'\nVocê jogou {player_num} e o Computador jogou {pc_num}. O Total foi {soma}\n' + '-'* 20)

    if player == 'P':
        if soma % 2 == 0:
            print('O Resultado foi Par. Você ganhou parabéns!')
            vitorias += 1
            print('Vamos Jogar Novamente...')
        else:
            result = False
            print('O Resultado foi Ímpar. Que pena você perdeu')
    elif player in 'IÍ':
        if soma % 2 != 0:
            print('O Resultado foi Ímpar. Você ganhou parabéns!')
            vitorias += 1
            print('Vamos Jogar Novamente...')
        else:
            result = False
            print('O Resultado foi Par. Que pena você perdeu')
    if not result:
        break
print(f'Você teve {vitorias} vitórias consecutivas! Parabéns!')
