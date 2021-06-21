from Uteis import mensagem, cores


def cadastrar(txt):
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
            idade = int(input('Digite a idade: '))
        except ValueError:
            cores(1, 'Erro! Digite um valor válido.')
        else:
            break

    txt.write(f'{nome}      {idade}\n')
    print(f'Novo registro de {nome} adicionado.')


def dados(txt):
    mensagem('Pessoas Cadastradas', 40)

    for linha in txt:
        valores = linha.split()
        nome = valores[:-1]
        nome_com = ''
        for pal in nome:
            nome_com += pal + ' '
        print(f'{nome_com:<29}{valores[-1]:<3} anos')
