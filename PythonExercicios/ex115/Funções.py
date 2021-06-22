from Uteis import mensagem, cores


def cadastrar():
    """
    -> Cadastra novas pessoa no 'banco de dados'
    :return: Sem retorno
    """
    try:
        inserir = open('Dados.txt', 'a')  # Abre o arquivo 'Dados' no modo de escrita
    except FileNotFoundError:
        cores(1, 'Erro ao tentar abrir o arquivo')
    else:
        mensagem('Novo Cadastro', 40)

        while True:
            try:
                nome = input('Digite o nome: ').strip()
            except ValueError:
                cores(1, 'Digite um valor válido.')
            else:
                break

        while True:
            try:
                idade = leia_int('Digite a idade: ')
            except ValueError:
                cores(1, 'Erro! Digite um valor válido.')
            else:
                break

        inserir.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado.')


def dados():
    """
    -> Mostra os dados armazenados no 'banco de dados'
    :return: Sem retorno
    """
    try:
        ler = open('Dados.txt', 'r')  # Abre o arquivo 'Dados' no modo leitura
    except FileNotFoundError:
        cores(1, 'Erro ao tentar ler o arquivo')
    else:
        mensagem('Pessoas Cadastradas', 40)

        for linha in ler:
            valores = linha.split(';')
            valores[1] = valores[1].replace('\n', '')
            print(f'{valores[0]:<29}{valores[1]:<3} anos')


def menu(lista):
    """
    -> Cria um menu com uma lista de opções
    :param lista: Lista de opções
    :return: Sem retorno
    """
    for item in range(0, len(lista)):
        cores(3, item+1, True), print(' - ', end=''), cores(4, lista[item])


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
            cores(1, 'O usuário preferiu não informar esse número!')
        except ValueError:
            cores(1, 'Erro! por favor, digite um número inteiro válido.')
