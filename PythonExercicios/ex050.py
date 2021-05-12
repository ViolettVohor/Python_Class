s = 0
for i in range(0, 6):  # Pede para o usuário digitar seis números inteiros e soma aquele que forem par
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'\033[7;1mA soma dos números pares que você digitou é \033[46;7;1m{s}\033[m')
