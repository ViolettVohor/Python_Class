def ajuda(func):
    help(func)


while True:
    print('\033[42;1m~' * 30)
    print(f'{"SISTEMA DE AJUDA PYTHON":^30}')
    print('~' * 30, end='\n\033[m')

    # noinspection SpellCheckingInspection
    funcao = input('Função ou Biblioteca >').strip()

    if funcao.upper() == 'FIM':
        print('\033[41;1m~'*20)
        print(f'{"Até Logo!":^20}')
        print('~'*20, end='\n\033[m')
        break

    print('\033[45;1m~' * 40)
    print(f'{f"Acessando o manual do comando {funcao}":^40}')
    print('~' * 40, end='\n\033[m')
    print('\033[7m')
    ajuda(funcao)
    print('\033[m')
