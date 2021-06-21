import Funções
from Uteis import linha, mensagem, cores

esc = 0

while esc != 3:
    mensagem('Menu Principal', 40)
    cores(3, '1', True), print(' - ', end=''), cores(4, 'Ver pessoas cadastradas')
    cores(3, '2', True), print(' - ', end=''), cores(4, 'Cadastrar novas pessoas')
    cores(3, '3', True), print(' - ', end=''), cores(4, 'Sair do Sistema')
    linha(40)

    inserir = open('Dados.txt', 'a')
    ler = open('Dados.txt', 'r')

    try:
        esc = int(input('\033[33;1mSua opção: \033[m'))
    except ValueError:
        cores(1, 'Erro! Digite uma opção válida.')

    if esc > 3 or esc < 0:
        cores(1, 'Erro! Digite uma opção válida.')

    if esc == 1:
        Funções.cadastrar(inserir)
    elif esc == 2:
        Funções.dados(ler)
