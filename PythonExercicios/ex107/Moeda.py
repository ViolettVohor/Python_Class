def aumentar(n=0, porc=0):
    """
    -> Calcula o aumento de um valor, utilizando porcentagem pré-determinada
    :param n: (opcional) Número a ser aumentado
    :param porc: (opcional) Porcentagem a ser utilizada
    :return: Retorna 'n' mais 'porc' porcento, ex: 10 + 20%
    """
    return n * (1 + porc/100)


def diminuir(n=0, porc=0):
    """
    -> Retorna um valor com um desconto pré-determinado
    :param n: (opcional) Números a receber o desconto
    :param porc: (opcional) Porcentagem a se descontada
    :return: Retorna o valor 'n' com o desconto
    """
    return n * (1 - porc/100)


def dobro(n=0):
    """
    -> Retorna o dobro do valor inserido
    :param n: (opcional) Número a ter seu valor dobrado
    :return: Retorna o dobro de 'n'
    """
    return n*2


def metade(n=0):
    """
    -> Retorna metade do valor inserido
    :param n: (opcional) Número a ser dividido
    :return: Retorna metade de 'n'
    """
    return n/2
