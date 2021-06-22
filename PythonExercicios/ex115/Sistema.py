import Funções as Func
from Uteis import linha, mensagem, cores
from time import sleep

esc = 0

while esc != 3:
    mensagem('Menu Principal', 40)
    menu = ['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema']
    Func.menu(menu)
    linha(40)

    # Caso o arquivo 'Dados' não exista, a função open() irá criar um arquivo novo

    try:
        esc = Func.leia_int('\033[33;1mSua opção: \033[m')
    except TypeError:
        cores(1, 'Erro! Digite um número inteiro válido')

    if esc == 1:
        Func.cadastrar()
    elif esc == 2:
        Func.dados()
    elif esc == 3:
        mensagem('Saindo do sistema... Até logo!', 40)
    else:
        cores(1, 'Erro! Digite uma opção válida.')

    sleep(1)
