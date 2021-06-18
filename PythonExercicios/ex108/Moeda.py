def aumentar(n, porc):
    """
    -> Calcula o aumento de um valor, utilizando porcentagem pré-determinada
    :param n: número a ser aumentado
    :param porc: porcentagem a ser utilizada
    :return: retorna 'n' mais 'porc' porcento, ex: 10 + 20%
    """
    return n * (1 + porc/100)


def diminuir(n, porc):
    """
    -> Retorna um valor com um desconto pré-determinado
    :param n: números a receber o desconto
    :param porc: porcentagem a se descontada
    :return: retorna o valor 'n' com o desconto
    """
    return n * (1 - porc/100)


def dobro(n):
    """
    -> Retorna o dobro do valor inserido
    :param n: Número a ter seu valor dobrado
    :return: Retorna o dobro de 'n'
    """
    return n*2


def metade(n):
    """
    -> Retorna metade do valor inserido
    :param n: Número a ser dividido
    :return: Retorna metade de 'n'
    """
    return n/2


def moeda(n):
    """
    -> Formata os valores monetários
    :param n: Valor a ser formatado
    :return: valor 'n' formatado
    """
    return f'R${n:.2f}'
