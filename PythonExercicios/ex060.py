# from math import factorial
n = int(input('Digite um número para Calcular seu Fatorial: '))
c = n
fat = 1
# fatorial = factorial(n)
print(f'O fatorial de {n}! =', end=' ')
while c != 0:
    print(c, end='')
    print(' x ' if c != 1 else ' = ', end='')
    fat *= c
    c -= 1
print(fat)

'''cont = n
for cont in range(cont, 0, -1):
    print(cont, end='')
    print(' x ' if cont != 1 else ' = ', end='')
    fat *= cont
print(fat)'''
