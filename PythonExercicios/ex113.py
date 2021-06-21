def leia_int(msg):
    """
    -> Utiliza a função 'input' e verifica se o valor introduzido é Inteiro
    :param msg: Mensagem a ser mostrada ao usuário
    :return: Retorna o valor digitado pelo usuário, caso o valor seja Inteiro
    """
    while True:
        try:
            return int(input(msg))
        except KeyboardInterrupt:
            print('\033[31;1mO usuário preferiu não informar esse número!')
        except ValueError:
            print('\033[31;1mErro! por favor, digite um número inteiro válido.\033[m')


def leia_float(msg):
    """
    -> Utiliza a função 'input' e verifica se o valor introduzido é Real
    :param msg: Mensagem a ser mostrada ao usuário
    :return: Retorna o valor digitado pelo usuário, caso o valor seja Real
    """
    while True:
        try:
            return float(input(msg))
        except KeyboardInterrupt:
            print('\033[31;1mO usuário preferiu não informar esse número!')
        except ValueError:
            print('\033[31;1mErro! por favor, digite um número real válido.\033[m')


nint = leia_int('Digite um Inteiro: ')
nfloat = leia_float('Digite um Real: ')
print(f'O valor inteiro foi {nint} e o real foi {nfloat}')
