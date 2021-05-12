idade_older = 0
nome_older = ''
idade_F_menos = 0
idade_soma = 0

for i in range(0, 5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    genero = input('Digite o seu gênero [M/F]: ').upper()
    print('')  # Cria um espaço entre cada pessoa
    if genero == 'M' and idade > idade_older:  # Verifica quem é o homem mais velho
        idade_older = idade
        nome_older = nome
    if genero == 'F' and idade < 20:  # Verifica quantas mulheres são menores de 20 anos
        idade_F_menos += 1
    idade_soma += idade

print(f'A média de idade é \033[7;1m{idade_soma/5}\033[m')
print(f'O homem mais velho é o \033[37;1m{nome_older}\033[m')
print(f'Têm \033[31;1m{idade_F_menos}\033[m mulheres mais novas que 20 anos')
