from time import sleep


def contador(i, f, p):
    if p == 0:  # Caso usuário digite 0 para o passo, ele é substituído por 1
        p = 1

    if p > 0 and f < i or p < 0 and f > i:
        # Caso o passo for negativo/[positivo] e o fim maior/[menor] que o começo, o seu sinal é invertido
        p *= -1

    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)

    if f > i:  # Se o fim for maior que o início, ele recebe mais um para que ele possa ser contado
        f += 1
    else:  # Se o fim for menor que o início, ele recebe menos um para que ele possa ser contado
       f -= 1

    for i in range(i, f, p):  # Mostra os números
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)  # Chama a função 'contador' que irá contar de 1 até 10 de 1 em 1

contador(10, 0, 2)  # Chama a função 'contador' que irá contar de 10 até 0 de 2 em 2

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
