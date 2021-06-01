from random import randint

result = True  # Variável que serve para parar o loop
vitorias = 0  # Conta o número de vitórias

print('-=-' * 10 + f'\n{"Vamos Jogar Par ou Ímpar":^30}')

while True:
    player = str(input('-=-' * 10 + '\nÍmpar ou Par? ')).upper().split()[0]

    if player not in 'IÍP':  # Se o Jogador não digitar I, Í ou P, o program vai pedir para que ele digite denovo
        # Não é a melhor solução, seguir exemplo ex070
        print('\nDigite Ímpar ou Par.\n')
        continue

    pc_num = randint(0, 10)  # Escolhe um número pro pc
    player_num = int(input('Digite um número entre 0 e 10: '))

    soma = pc_num + player_num

    print('-' * 20 + f'\nVocê jogou {player_num} e o Computador jogou {pc_num}. O Total foi {soma}\n' + '-' * 20)

    if player == 'P':  # Se o jogador escolheu par
        if soma % 2 == 0:  # Se a soma for Par, o jogador ganha e o jogo continua
            print('O Resultado foi Par. Você ganhou parabéns!')
            vitorias += 1
            print('Vamos Jogar Novamente...')
        else:  # Se a soma for Ímpar, o jogador perde e o program encerra
            result = False
            print('O Resultado foi Ímpar. Que pena você perdeu')
    elif player in 'IÍ':  # Se o jogador escolher Ímpar
        if soma % 2 != 0:  # Se a soma for Ímpar, o jogador ganha e o jogo continua
            print('O Resultado foi Ímpar. Você ganhou parabéns!')
            vitorias += 1
            print('Vamos Jogar Novamente...')
        else:  # Se a soma for Par, o jogador perde e o program encerra
            result = False
            print('O Resultado foi Par. Que pena você perdeu')
    if not result:  # Result for False, encerra o loop
        break
print(f'Você teve {vitorias} vitórias consecutivas! Parabéns!')
