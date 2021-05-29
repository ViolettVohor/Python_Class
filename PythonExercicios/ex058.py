from random import randint
pc = randint(0, 10)
player = 11
cont = 0
while player != pc:
    player = int(input('Tente adivinhar qual número eu escolhi entre 0 e 10: '))
    if player != pc:
        print('Errou tente denovo!')
    else:
        print('Parabéns você acertou!')
    cont += 1
print(f'Você precisou de {cont} tentativas para acertar!')
