from random import randint

pc = randint(0, 10)
# Escolhe um número entre 0 e 10 para o pc
player = int(input('Tente adivinhar qual número eu escolhi entre 0 e 10: '))
cont = 0  # variável para contar quantas vezes o player tentou acertar o número
print('-'*25)

while player != pc:  # Enquanto o jogador não acertar o número que o pc 'escolheu'
    if player > pc:  # Se o jogador digitar um número maior que o do pc
        player = int(input('\033[36;1mMenos...\033[m tente denovo! \nQual o seu palpite? '))
    elif player < pc:  # Se o jogador digite um número menor que o do pc
        player = int(input('\033[37;1mMais..\033[m tente denovo! \nQual o seu palpite? '))
    cont += 1  # Conta o número de tentativas
    print('-' * 25)
print(f'\033[32;1mParabéns\033[m você acertou! \nVocê precisou de \033[35;1m{cont}\033[m tentativas para acertar!')
