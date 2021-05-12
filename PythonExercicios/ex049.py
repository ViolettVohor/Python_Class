n = int(input('Digite um número inteiro: '))
# Pede para que o usuário digite um número e armazena na variável

print('\033[34;1m-' * 12)
# Cria um traçado e deixa todos os caracteres a partir do traçado na magenta

for i in range(0, 11):
    print(f' {i} x {n} = \033[1;36m{n * i}\033[34;1m')
# Mostra a tabuado do número digitado pelo usuário

print('-' * 12)
# Cria outro traçado
