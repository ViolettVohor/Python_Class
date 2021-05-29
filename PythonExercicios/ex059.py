c = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
while c != 5:
    c = int(input('\n[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Introduzir novos números\n'
                  '[5] Sair do programa\n'))
    if c == 1:
        print(f'a soma desses números é {n1 + n2}')
    elif c == 2:
        print(f'a multiplicação desses números é {n1 * n2}')
    elif c == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'o maior número é {maior}')
    elif c == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um segundo número: '))
    else:
        print('Fim')
