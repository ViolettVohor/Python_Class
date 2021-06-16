def leia_int(txt):
    """
    -> Verifica se o valor digitado é numérico
    :param txt: mensagem a ser mostrado para o usuário
    :return: retorna o valor digitado pelo o usuário, caso seja um número
    """
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        else:
            print('\033[31;1mERRO! Digite um número.\033[m')
    return num


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
