print('Gerador de PA\n' + '-='*7)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
limite = 10  # Limite inicial dos termos
cont = 0  # Index dos termos
mais = 1  # Limite adicionado pelo usuário

while mais != 0:
    while cont < limite:
        print(a1, end=' -> ')
        a1 += r
        cont += 1
        '''if cont == n:  # Substituí o 'while mais != 0:'
            print('PAUSA')
            n += int(input('Você quer que repita mais quantas vezes? '))'''
    print('PAUSA')
    mais = int(input('Você quer que repita mais quantas vezes? '))
    limite += mais
print(f'Progressão finalizada com {cont} termos mostrados')
