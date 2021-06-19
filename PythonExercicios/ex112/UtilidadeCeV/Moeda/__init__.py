def aumentar(n=0, porc=0, form=False):
    """
    -> Calcula o aumento de um valor, utilizando porcentagem pré-determinada
    :param n: (opcional) Número a ser aumentado
    :param porc: (opcional) Porcentagem a ser utilizada
    :param form: (opcional) Caso verdadeiro formata o valor, utilizando a função moeda
    :return: Retorna 'n' mais 'porc' porcento, ex: 10 + 20%
    """
    num = n * (1 + porc/100)
    return num if not form else moeda(num)


def diminuir(n=0, porc=0, form=False):
    """
    -> Retorna um valor com um desconto pré-determinado
    :param n: (opcional) Números a receber o desconto
    :param porc: (opcional) Porcentagem a se descontada
    :param form: (opcional) Caso verdadeiro formata o valor, utilizando a função moeda
    :return: Retorna o valor 'n' com o desconto
    """
    num = n * (1 - porc/100)
    return num if not form else moeda(num)


def dobro(n=0, form=False):
    """
    -> Retorna o dobro do valor inserido
    :param n: (opcional) Número a ter seu valor dobrado
    :param form: (opcional) Caso verdadeiro formata o valor, utilizando a função moeda
    :return: Retorna o dobro de 'n'
    """
    num = n*2
    return num if not form else moeda(num)


def metade(n=0, form=False):
    """
    -> Retorna metade do valor inserido
    :param n: (opcional) Número a ser dividido
    :param form: (opcional) Caso verdadeiro formata o valor, utilizando a função moeda
    :return: Retorna metade de 'n'
    """
    num = n/2
    return num if not form else moeda(num)


def moeda(n, moeda='R$'):
    """
    -> Formata os valores monetários
    :param n: Valor a ser formatado
    :param moeda: (opcional) Moeda a ser utilizada na formatação
    :return: Valor 'n' formatado
    """
    return f'{moeda}{n:.2f}'


def resumo(n=0, porc_aum=10, porc_des=5):
    """
    -> Mostra um resumo do preço inserido
    :param n: (opcional) Preço a ser utilizado
    :param porc_aum: (opcional) Porcentagem do aumento
    :param porc_des: (opcional) Porcentagem do desconto
    :return: Sem retorno
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))  # Centraliza o texto
    print('-'*30)

    print(f'Preço analisado: \t{moeda(n)}')  # '\t' Cria uma tabulação
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{porc_aum}% de aumento: \t{aumentar(n, porc_aum, True)}')
    print(f'{porc_des}% de desconto: \t{diminuir(n, porc_des, True)}')

    print('-'*30)
