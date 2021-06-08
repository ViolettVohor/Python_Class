matriz = [[], [], []]
# noinspection SpellCheckingInspection
somapar = somacol = somalin = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um número para [{lin}, {col}]: ')))
        if matriz[lin][col] % 2 == 0:
            somapar += matriz[lin][col]

print('-='*30)
for lin in matriz:
    # noinspection SpellCheckingInspection
    for icol, col in enumerate(lin):
        print(f'[  {col}  ]', end=' ')
        if icol == 2:
            somacol += col
    print()

print('-='*30)
print(f'A soma de todos os valores pares vale {somapar}')
print(f'A soma de todos os valores da terceira coluna vale {somacol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
