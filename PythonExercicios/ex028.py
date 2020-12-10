from random import randint
from time import sleep
n = randint(0, 5)
print('=-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
resp = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2)
print('Parabéns, você acertou!' if n == resp else f'Você errou, eu pensei em {n}')
