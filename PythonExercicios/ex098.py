from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1

    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(0.5)

    if f > i:
        f += 1
        passo = p
    else:
        f -= 1
        if p > 0:
            passo = p - p - p
        else:
            passo = p

    for i in range(i, f, passo):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)

contador(10, 0, 2)

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
