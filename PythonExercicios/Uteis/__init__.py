def linha(tam=20):
    """
    -> Cria uma linha
    :param tam: (opcional) Determina o tamanho da linha
    :return: Sem retorno
    """
    print('-'*tam)


def mensagem(txt, tam=20):
    """
    -> Cria uma mensagem com duas linhas
    :param txt: Mensagem a ser escrita
    :param tam: Tamanho da linha
    :return: Sem retorno
    """
    linha(tam)
    print(txt.center(tam))
    linha(tam)


def cores(cor, msg, quebra=False):
    """
    -> Cria uma mensagem colorida
    :param cor: Determina a cor da mensagem
    :param msg: Mensagem a ser escrita
    :param quebra: Determina se ela criará uma quebra no final da linha
    :return: Sem retorno
    """
    colors = ['\033[30;1m',  # 0 - Branco
              '\033[31;1m',  # 1 - Vermelho
              '\033[32;1m',  # 2 - Verde
              '\033[33;1m',  # 3 - Amarelo
              '\033[34;1m',  # 4 - Azul
              '\033[35;1m',  # 5 - Magenta
              '\033[36;1m',  # 6 - Cinza
              '\033[m'       # 7 - limpar
              ]
    if not quebra:
        print(f'{colors[cor]}{msg}{colors[7]}')
    else:
        print(f'{colors[cor]}{msg}{colors[7]}', end='')
