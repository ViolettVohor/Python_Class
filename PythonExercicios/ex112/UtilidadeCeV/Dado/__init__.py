def leia_dinheiro(msg):
    """
    -> Recebe um valor digitado pelo usuário e verifica se é um
    valor númerico válido
    :param msg: Mensagem a ser mostrada ao usuário
    :return: Retorno o valor digitado pelo usuário caso seja válido
    """
    while True:
        num = input(msg).strip().replace(',', '.')  # Substitui as vírgulas por pontos
        if num.replace('.', '').isdigit():  # 'Exluí' os pontos
            num = float(num)
            break
        else:
            print(f'\033[1;31mERRO! \"{num}\" não é um preço válido.\033[m')
    return num
