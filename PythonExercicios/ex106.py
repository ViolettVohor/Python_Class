c = ('\033[m',          # 0 - Sem cor
     '\033[30;41;1m',   # 1 - Vermelho
     '\033[30;42;1m',   # 2 - Verde
     '\033[30;43;1m',   # 3 - Amarelho
     '\033[30;44;1m',   # 4 - Azul
     '\033[30;45;1m',   # 5 - Magenta
     '\033[7;30m'       # 6 - Branco
     )


def ajuda(func):
    """
    -> Função que mostra o help de uma função formatado
    :param func: Nome da função a ser mostrado o help
    :return: sem retorno
    """
    from time import sleep
    print(c[6], end='')
    sleep(0.5)
    help(func)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    """
    -> Recebe um título e formata ele
    :param msg: Título a ser formatado
    :param cor: cor a se utilizada no fundo
    :return: sem retorno
    """
    tam = len(msg) + 10
    print(c[cor] + '~' * tam)
    print(f'     {msg}     ')
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PYTHON', 2)

    # noinspection SpellCheckingInspection
    funcao = input('Função ou Biblioteca >').strip()

    if funcao.upper() == 'FIM':
        titulo('Até Logo!', 1)
        break

    titulo(f'Acessando o manual do comando \'{funcao}\'', 5)
    # A barra invertida permite que a aspa seja impresssa, sem atrapalhar a string

    ajuda(funcao)
