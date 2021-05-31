from random import randint
pc = randint(0, 10)
player = int(input('Tente adivinhar qual número eu escolhi entre 0 e 10: '))
cont = 0
while player != pc:
    if player > pc:
        player = int(input('Menos... tente denovo! \nQual o seu palpite? '))
    elif player < pc:
        player = int(input('Mais.. tente denovo! \nQual o seu palpite? '))
    cont += 1
print(f'Parabéns você acertou! \nVocê precisou de {cont} tentativas para acertar!')
