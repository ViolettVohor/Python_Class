from random import choice
print('-' * 20)
print(f'{"JOKENPÔ":^20}')
print('-' * 20)

pla = int(input('1 - Papel'
                '\n2 - Pedra'
                '\n3 - Tesoura'
                '\nEscolha um número: '))
cho = ['Papel', 'Pedra', 'Tesoura']
com = str(choice(cho))

if pla == 1:
    pla = 'Papel'
elif pla == 2:
    pla = 'Pedra'
elif pla == 3:
    pla = 'Tesoura'
else:
    exit('Escolha um número válido')

if pla == com:
    res = '\033[37;1mEmpate'
elif pla == 'Papel' and com == 'Pedra' or pla == 'Pedra' and com == 'Tesoura' or pla == 'Tesoura' and com == 'Papel':
    res = '\033[32;1mO Player Venceu'
else:
    res = '\033[31;1mO Computador Venceu'

print(f'Você escolheu \033[36;3m{pla}\033[m, o computador \033[35;3m{com}\033[m e o resultado dessa disputa foi {res}')
