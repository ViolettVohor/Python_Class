def fatorial(num):
    """
    -> Calcula o fatorial de um número
    :param num: Número que terá o fatorial calculado
    :return: retorna o fatorial de 'num'
    """
    f = 1
    for c in range(1, num+1):
        f *= c
    return f


def dobro(num):
    """
    -> Calcula o dobro de um número
    :param num: Número que terá seu dobro calculado
    :return: retorna o dobro de 'num'
    """
    return num*2


def triplo(num):
    """
    -> Calcula o triplo de um número
    :param num: Número que terá seu triplo calculado
    :return: retorna o triplo    de 'num'
    """
    return num*3
