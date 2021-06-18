def aumentar(n, porc, form=False):
    """
    -> Calcula o aumento de um valor, utilizando porcentagem pré-determinada
    :param n: número a ser aumentado
    :param porc: porcentagem a ser utilizada
    :param form: (opcional) Caso verdadeiro formata o valor
    :return: retorna 'n' mais 'porc' porcento, ex: 10 + 20%
    """
    num = n * (1 + porc/100)
    if form:
        num = moeda(num)
    return num


def diminuir(n, porc, form=False):
    """
    -> Retorna um valor com um desconto pré-determinado
    :param n: números a receber o desconto
    :param porc: porcentagem a se descontada
    :param form: (opcional) Caso verdadeiro formata o valor
    :return: retorna o valor 'n' com o desconto
    """
    num = n * (1 - porc/100)
    if form:
        num = moeda(num)
    return num


def dobro(n, form=False):
    """
    -> Retorna o dobro do valor inserido
    :param n: Número a ter seu valor dobrado
    :param form: (opcional) Caso verdadeiro formata o valor
    :return: Retorna o dobro de 'n'
    """
    num = n*2
    if form:
        num = moeda(num)
    return num


def metade(n, form=False):
    """
    -> Retorna metade do valor inserido
    :param n: Número a ser dividido
    :param form: (opcional) Caso verdadeiro formata o valor
    :return: Retorna metade de 'n'
    """
    num = n/2
    if form:
        num = moeda(num)
    return num


def moeda(n):
    """
    -> Formata os valores monetários
    :param n: Valor a ser formatado
    :return: valor 'n' formatado
    """
    return f'R${n:.2f}'


def resumo(n, porc_aum, porc_des):
    """
    -> Mostra um resumo do preço inserido
    :param n: Preço a ser utilizado
    :param porc_aum: Porcentagem do aumento
    :param porc_des: Porcentagem do desconto
    :return: Sem retorno
    """
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)

    print(f'{"Preço analisado:":<20}' + moeda(n))
    print(f'{"Dobro do preço:":<20}' + dobro(n, True))
    print(f'{"Metade do preço:":<20}' + metade(n, True))
    print(f'{f"{porc_aum}% de aumento:":<20}' + aumentar(n, porc_aum, True))
    print(f'{f"{porc_des}% de desconto:":<20}' + diminuir(n, porc_des, True))

    print('-'*30)
