# from math import factorial
n = int(input('Digite um número para Calcular seu Fatorial: '))
c = n  # Recebe o valor do variável n, essa variável será usada para calcular o fatorial
fat = 1
# fatorial = factorial(n)  # função que calcular o fatorial de um número

print(f'O fatorial de \033[33;1m{n}!\033[m =', end=' ')
while c != 0:
    print(f'\033[34;1m{c}\033[m', end='')
    print(' x ' if c != 1 else ' = ', end='')
    fat *= c  # multiplica o valor de fat pelo valor de c e no final temos a fatorial
    c -= 1
print(f'\033[37;1m{fat}\033[m')

'''cont = n
for cont in range(cont, 0, -1):  # Igual ao laço acima, mas utilizando for
    print(cont, end='')
    print(' x ' if cont != 1 else ' = ', end='')
    fat *= cont
print(fat)'''
