from time import sleep


def fatorial(num, show=False):
    """
    -> O fatorial calcula o fatorial de um número
    :param num: O número a ser calculado o fatorial
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    fat = 1
    print('-'*30)
    if show:
        print('Os cálculos são: ', end='')

    for c in range(num, 0, -1):
        fat *= c
        if show:
            sleep(0.5)
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return fat


print(fatorial(5, True))
