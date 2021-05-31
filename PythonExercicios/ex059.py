from time import sleep
op = 0
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while op != 5:
    op = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Introduzir novos números
    [5] Sair do programa
>>>>> Qual a sua opção? '''))
    if op == 1:
        print(f'O resultado da soma {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'O resultado da multiplicação {n1} X {n2} é {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior número é {maior}')
    elif op == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    print('=-=' * 10)
sleep(2)
print('Fim do programa.')
