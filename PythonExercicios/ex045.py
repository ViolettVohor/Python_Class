from random import choice
from time import sleep
print('-' * 20)
print(f'{"JOKENPÔ":^20}')
print('-' * 20)

pla = int(input('1 - Papel'
                '\n2 - Pedra'
                '\n3 - Tesoura'
                '\nEscolha um número: '))
cho = ['Papel', 'Pedra', 'Tesoura']
com = str(choice(cho))

if 1 > pla or pla > 3:
    exit('Escolha um número válido')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if cho[pla - 1] == com:
    res = '\033[37;1mEmpate'
elif pla == 1 and com == 'Pedra' or pla == 2 and com == 'Tesoura' or pla == 3 and com == 'Papel':
    res = '\033[32;1mO Player Venceu'
else:
    res = '\033[31;1mO Computador Venceu'

print(f'Você escolheu \033[36;3m{cho[pla - 1]}\033[m, o computador \033[35;3m{com}'
      f'\033[m e o resultado dessa disputa foi {res}')
