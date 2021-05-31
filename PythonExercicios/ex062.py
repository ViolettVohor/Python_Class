print('Gerador de PA\n' + '-='*7)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 10
cont = 0
mais = 1

while mais != 0:
    while cont < n:
        print(a1, end=' -> ')
        a1 += r
        cont += 1
        '''if cont == n:
            print('PAUSA')
            n += int(input('Você quer que repita mais quantas vezes? '))'''
    print('PAUSA')
    mais = int(input('Você quer que repita mais quantas vezes? '))
    n += mais
print(f'Progressão finalizada com {cont} termos mostrados')
