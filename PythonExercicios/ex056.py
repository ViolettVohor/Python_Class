idade_older = 0
nome_older = ''
idade_F_menos = 0
idade_soma = 0

for i in range(1, 5 ):
    # Lê dados de 5 pessoas e mostra a média de idades, o homem mais velho
    # e a quantidade de mulheres que tem menos de 20 anos
    print('-'*7, f'{i}° pessoa', '-'*7)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    genero = input('Gênero [M/F]: ')
    print('')  # Cria um espaço entre cada pessoa
    if genero in 'Mm' and idade > idade_older:  # Verifica quem é o homem mais velho
        idade_older = idade
        nome_older = nome
    if genero in 'Ff' and idade < 20:  # Verifica quantas mulheres são menores de 20 anos
        idade_F_menos += 1
    idade_soma += idade

print(f'A média de idade é \033[7;1m{idade_soma/i}\033[m')
print(f'O homem mais velho é o \033[37;1m{nome_older}\033[m e ele tem {idade_older} anos')
print(f'Têm \033[31;1m{idade_F_menos}\033[m mulheres mais novas que 20 anos')
