def fatorial(num, show=False):
    """
    -> O fatorial calcula o fatorial de um número
    :param num: O número a ser calculado o fatorial
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    from time import sleep
    fat = 1
    print('-'*30)
    if show:
        print('Os cálculos são: ', end='')

    for c in range(num, 0, -1):
        fat *= c  # Calcula o fatorial
        if show:  # Caso show seja True, mostra o calculo do fatorial
            print(c, end='')
            sleep(0.5)
            if c != 1:
                print(end=' x ')
            else:
                print(end=' = ')
    return fat


print(fatorial(5, True))
