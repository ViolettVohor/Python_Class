n = int(input('Digite um número inteiro: '))
p = 0
for i in range(1, n + 1):  # Verifica se o número que o usuário digitou é primo
    if n % i == 0:
        p += 1
        print(f'\033[33;1m', end='')
    else:
        print(f'\033[31;1m', end='')
    print(i, end=' \033[m')

print(f'\nO número {n} foi divisível {p} vezes')
if p == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
