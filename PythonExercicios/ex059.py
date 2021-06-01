from time import sleep

op = 0  # Variável que representa as opções
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

while op != 5:  # Enquanto op não receber o valor 5
    op = int(input('''    \033[37;1m[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Introduzir novos números
    [5] Sair do programa\033[m
>>>>> Qual a sua opção? '''))
    # Criar um menu que mostrar as opções que o programa pode executar

    if op == 1:  # Se op receber 1 então mostra a soma entre os números
        print(f'O resultado da\033[36;1m soma {n1} + {n2} é {n1 + n2}\033[m')
    elif op == 2:  # Se op recebe 2 então mostra a multiplicação entre os números
        print(f'O resultado da\033[33;1m multiplicação {n1} X {n2} é {n1 * n2}\033[m')
    elif op == 3:  # Se op recebe 3 então mostra o maior entre os dois número
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2},\033[30;1m o maior número é {maior}\033[m')
    elif op == 4:  # Se op recebe 4 então o usuário pode inserir novos números
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:  # Se op recebe 5 então o programa é finalizado
        print('Finalizando...')
    else:
        print('\033[31mOpção inválida.\033[m')
    print('=-=' * 10)

sleep(2)  # Pausa o programa por 2 segundos
print('Fim do programa.')
